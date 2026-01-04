#!/usr/bin/env python3
"""
Combined script to update all project documentation.
This script:
1. Fetches all repositories
2. Generates/updates markdown files with enhanced info
3. Fixes language display issues
4. Updates mkdocs.yml navigation
"""

import json
import subprocess
import os
from datetime import datetime

def run_gh_command(cmd):
    """Run a gh CLI command and return the output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error: {e.stderr}")
        return None

def get_all_repos(username="aaron777collins"):
    """Fetch all public repositories for the user."""
    print(f"Fetching all repositories for {username}...")
    cmd = f'gh repo list {username} --limit 200 --json name,description,url,isPrivate,primaryLanguage,stargazerCount,forkCount,createdAt,updatedAt,homepageUrl,isArchived,isFork'
    output = run_gh_command(cmd)

    if not output:
        return []

    try:
        repos = json.loads(output)
        # Filter to only public repos
        public_repos = [r for r in repos if not r.get('isPrivate', False)]
        print(f"Found {len(public_repos)} public repositories")
        return public_repos
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def get_repo_details(repo_name):
    """Get detailed information about a repository."""
    print(f"  Fetching details for {repo_name}...")

    # Get repository details
    details_cmd = f'gh api repos/aaron777collins/{repo_name} --jq \'{{name, description, html_url, homepage, created_at, updated_at, stargazers_count, forks_count, language, archived, fork, license: .license.name, topics}}\''
    details_output = run_gh_command(details_cmd)

    if not details_output:
        return None

    try:
        details = json.loads(details_output)
    except json.JSONDecodeError:
        print(f"  ⚠ Could not parse details for {repo_name}")
        return None

    # Get languages
    languages_cmd = f'gh api repos/aaron777collins/{repo_name}/languages'
    languages_output = run_gh_command(languages_cmd)

    languages = []
    if languages_output:
        try:
            lang_data = json.loads(languages_output)
            if lang_data:
                # Sort by bytes of code (descending)
                sorted_langs = sorted(lang_data.items(), key=lambda x: x[1], reverse=True)
                languages = [lang[0] for lang in sorted_langs[:10]]  # Top 10 languages
        except json.JSONDecodeError:
            pass

    if not languages:
        languages = ["Not specified"]

    # Get latest release
    releases_cmd = f'gh api repos/aaron777collins/{repo_name}/releases/latest --jq \'{{name, tag_name, published_at, html_url}}\''
    releases_output = run_gh_command(releases_cmd)

    latest_release = None
    if releases_output and releases_output != "null":
        try:
            latest_release = json.loads(releases_output)
        except json.JSONDecodeError:
            pass

    # Check for GitHub Pages
    pages_cmd = f'gh api repos/aaron777collins/{repo_name}/pages --jq \'.html_url\''
    pages_output = run_gh_command(pages_cmd)
    github_pages_url = pages_output if pages_output and pages_output != "null" else None

    # Get README preview
    readme_cmd = f'gh api repos/aaron777collins/{repo_name}/readme --jq \'.content\' | base64 -d | head -c 500'
    readme_output = run_gh_command(readme_cmd)
    readme_preview = readme_output if readme_output else details.get('description', '')

    return {
        'name': details['name'],
        'description': details.get('description', ''),
        'url': details['html_url'],
        'homepage': details.get('homepage', ''),
        'created_at': details['created_at'],
        'updated_at': details['updated_at'],
        'stars': details.get('stargazers_count', 0),
        'forks': details.get('forks_count', 0),
        'language': details.get('language', 'Not specified'),
        'languages': languages,
        'archived': details.get('archived', False),
        'fork': details.get('fork', False),
        'license': details.get('license', 'Not specified'),
        'topics': details.get('topics', []),
        'latest_release': latest_release,
        'github_pages_url': github_pages_url,
        'readme_preview': readme_preview
    }

def format_date(date_str):
    """Format ISO date string to readable format."""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%B %d, %Y')
    except:
        return date_str

def generate_markdown(repo_details):
    """Generate markdown content for a repository."""
    name = repo_details['name']
    description = repo_details.get('description', 'No description provided.')
    url = repo_details['url']
    homepage = repo_details.get('homepage', '')
    created = format_date(repo_details.get('created_at', ''))
    updated = format_date(repo_details.get('updated_at', ''))
    stars = repo_details.get('stars', 0)
    forks = repo_details.get('forks', 0)
    language = repo_details.get('language', 'Not specified')
    languages = repo_details.get('languages', ['Not specified'])
    archived = repo_details.get('archived', False)
    fork = repo_details.get('fork', False)
    license_info = repo_details.get('license', 'Not specified')
    topics = repo_details.get('topics', [])
    latest_release = repo_details.get('latest_release')
    github_pages = repo_details.get('github_pages_url')
    readme_preview = repo_details.get('readme_preview', description)

    md_content = f"# {name}\n\n"

    # Badges
    badges = []
    if stars > 0:
        badges.append(f"⭐ {stars} stars")
    if forks > 0:
        badges.append(f"🔱 {forks} forks")
    if archived:
        badges.append("📦 Archived")
    if fork:
        badges.append("🔀 Fork")

    if badges:
        md_content += " | ".join(badges) + "\n\n"

    # Quick Links
    md_content += "## 🔗 Quick Links\n\n"
    md_content += f"- [View on GitHub]({url})\n"
    if homepage:
        md_content += f"- [Project Homepage]({homepage})\n"
    if github_pages:
        md_content += f"- [GitHub Pages Site]({github_pages})\n"
    if latest_release:
        release_name = latest_release.get('name', latest_release.get('tag_name', 'Latest Release'))
        release_url = latest_release.get('html_url', '')
        release_date = format_date(latest_release.get('published_at', ''))
        md_content += f"- [Latest Release: {release_name}]({release_url}) ({release_date})\n"

    md_content += "\n"

    # Project Details
    md_content += "## 📊 Project Details\n\n"
    md_content += f"- **Primary Language:** {language}\n"
    md_content += f"- **Languages Used:** {', '.join(languages)}\n"
    md_content += f"- **License:** {license_info}\n"
    md_content += f"- **Created:** {created}\n"
    md_content += f"- **Last Updated:** {updated}\n"

    md_content += "\n"

    # Topics
    if topics:
        md_content += "## 🏷️ Topics\n\n"
        md_content += ", ".join([f"`{topic}`" for topic in topics])
        md_content += "\n\n"

    # About
    md_content += "## 📝 About\n\n"
    if readme_preview:
        md_content += readme_preview[:500]
        if len(readme_preview) > 500:
            md_content += "..."
    else:
        md_content += description or "No description available."

    md_content += "\n\n"

    # Status notices
    if archived:
        md_content += "## ℹ️ Status\n\n"
        md_content += "⚠️ This repository is archived and no longer maintained.\n\n"

    if fork:
        md_content += "## ℹ️ Fork Information\n\n"
        md_content += "This is a fork of another repository.\n\n"

    return md_content

def update_mkdocs_nav(repos):
    """Update mkdocs.yml with all repositories organized by language."""
    print("\nUpdating mkdocs.yml navigation...")

    # Group repos by primary language
    by_language = {}
    featured = []

    for repo in repos:
        lang = repo.get('language', 'Other')
        if lang == 'Not specified' or not lang:
            lang = 'Other'

        if lang not in by_language:
            by_language[lang] = []
        by_language[lang].append(repo)

        # Add to featured if it has stars
        if repo.get('stars', 0) > 0:
            featured.append(repo)

    # Sort featured by stars (descending)
    featured.sort(key=lambda x: x.get('stars', 0), reverse=True)
    featured = featured[:15]  # Top 15

    # Read current mkdocs.yml
    with open('mkdocs.yml', 'r') as f:
        lines = f.readlines()

    # Find the nav section
    nav_start = -1
    for i, line in enumerate(lines):
        if line.strip() == 'nav:':
            nav_start = i
            break

    if nav_start == -1:
        print("Error: Could not find nav section in mkdocs.yml")
        return

    # Build new nav section
    nav_lines = ["nav:\n", "  - Home: index.md\n"]

    # Add Featured Projects
    if featured:
        nav_lines.append("  - Featured Projects:\n")
        for repo in featured:
            nav_lines.append(f"    - {repo['name']}: {repo['name']}.md\n")

    # Add All Projects by Language
    nav_lines.append("  - All Projects:\n")
    for lang in sorted(by_language.keys()):
        nav_lines.append(f"    - {lang}:\n")
        for repo in sorted(by_language[lang], key=lambda x: x['name'].lower()):
            nav_lines.append(f"      - {repo['name']}: {repo['name']}.md\n")

    # Replace nav section
    new_lines = lines[:nav_start] + nav_lines

    with open('mkdocs.yml', 'w') as f:
        f.writelines(new_lines)

    print(f"✓ Updated mkdocs.yml with {len(repos)} projects")

def main():
    """Main function to update all project documentation."""
    print("=" * 60)
    print("UPDATING ALL PROJECT DOCUMENTATION")
    print("=" * 60)
    print()

    # Fetch all repositories
    repos = get_all_repos()
    if not repos:
        print("Error: Could not fetch repositories")
        return 1

    print(f"\nProcessing {len(repos)} repositories...\n")

    # Ensure docs directory exists
    os.makedirs('docs', exist_ok=True)

    # Process each repository
    detailed_repos = []
    for i, repo in enumerate(repos, 1):
        repo_name = repo['name']
        print(f"[{i}/{len(repos)}] Processing {repo_name}...")

        # Get detailed information
        details = get_repo_details(repo_name)
        if not details:
            print(f"  ⚠ Skipping {repo_name} (could not fetch details)")
            continue

        # Store for nav update
        detailed_repos.append(details)

        # Generate markdown
        md_content = generate_markdown(details)

        # Write to file
        output_file = f"docs/{repo_name}.md"
        with open(output_file, 'w') as f:
            f.write(md_content)

        print(f"  ✓ Created {output_file}")

    # Update mkdocs.yml
    update_mkdocs_nav(detailed_repos)

    print()
    print("=" * 60)
    print(f"COMPLETE! Updated {len(detailed_repos)} project pages")
    print("=" * 60)

    return 0

if __name__ == "__main__":
    exit(main())
