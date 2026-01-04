#!/usr/bin/env python3
"""Fix the languages field in all markdown files"""

import os
import re
import subprocess
import json
import time

def get_repo_languages(repo_name):
    """Fetch languages for a repository using gh CLI"""
    try:
        result = subprocess.run(
            ['gh', 'api', f'repos/aaron777collins/{repo_name}/languages'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            languages = json.loads(result.stdout)
            if languages:
                # Sort by bytes of code (descending)
                sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
                return [lang for lang, _ in sorted_langs]
        return []
    except Exception as e:
        print(f"Error fetching languages for {repo_name}: {e}")
        return []

def fix_markdown_file(filepath):
    """Fix the languages line in a markdown file"""

    # Extract repo name from filename
    repo_name = os.path.basename(filepath).replace('.md', '')

    print(f"Processing {repo_name}...")

    # Read the file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if it has the broken languages pattern
    if '- **Languages Used:** , , ,' not in content and '- **Languages Used:** , ,' not in content:
        print(f"  ✓ Skipping {repo_name} - no broken languages")
        return False

    # Fetch languages from GitHub
    languages = get_repo_languages(repo_name)
    time.sleep(0.5)  # Rate limiting

    if languages:
        languages_str = ', '.join(languages)
        print(f"  ✓ Found languages: {languages_str}")
    else:
        languages_str = "Not specified"
        print(f"  ⚠ No languages found, using 'Not specified'")

    # Replace the broken languages line
    content = re.sub(
        r'- \*\*Languages Used:\*\* (?:, )+',
        f'- **Languages Used:** {languages_str}',
        content
    )

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Fixed {repo_name}")
    return True

def main():
    docs_dir = 'docs'
    fixed_count = 0

    # Get all markdown files
    md_files = [f for f in os.listdir(docs_dir) if f.endswith('.md') and f != 'index.md']

    print(f"Found {len(md_files)} markdown files to check\n")

    for md_file in sorted(md_files):
        filepath = os.path.join(docs_dir, md_file)
        if fix_markdown_file(filepath):
            fixed_count += 1

    print(f"\n✅ Fixed {fixed_count} files!")

if __name__ == '__main__':
    main()
