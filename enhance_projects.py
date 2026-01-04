#!/usr/bin/env python3
import json
import subprocess
import os
from datetime import datetime

def run_gh_command(cmd):
    """Run a gh CLI command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        return None
    except Exception as e:
        print(f"Error running command: {e}")
        return None

def get_repo_details(repo_name):
    """Fetch detailed information about a repository"""
    print(f"Fetching details for {repo_name}...")
    
    details = {}
    
    # Get basic repo info
    repo_info = run_gh_command(f'gh repo view {repo_name} --json name,description,url,homepageUrl,createdAt,updatedAt,pushedAt,stargazerCount,forkCount,isArchived,isFork,primaryLanguage,languages,repositoryTopics,hasIssuesEnabled,hasWikiEnabled,licenseInfo,defaultBranchRef')
    if repo_info:
        details.update(repo_info)
    
    # Get latest release
    release = run_gh_command(f'gh release view --repo {repo_name} --json tagName,name,publishedAt,url 2>/dev/null || echo null')
    if release and release != 'null':
        details['latestRelease'] = release
    
    # Check for GitHub Pages (look for gh-pages branch or Pages settings)
    branches = run_gh_command(f'gh api repos/{repo_name}/branches --jq ".[].name" 2>/dev/null')
    if branches:
        details['branches'] = branches
    
    # Try to get Pages info
    pages = run_gh_command(f'gh api repos/{repo_name}/pages 2>/dev/null')
    if pages:
        details['pages'] = pages
    
    # Get README content (first 500 chars for better description)
    readme = subprocess.run(f'gh repo view {repo_name} --json readme -q .readme', shell=True, capture_output=True, text=True)
    if readme.returncode == 0 and readme.stdout.strip():
        details['readmePreview'] = readme.stdout.strip()[:500]
    
    return details

def generate_enhanced_markdown(repo_details):
    """Generate enhanced markdown file for a repository"""
    name = repo_details.get('name', 'Unknown')
    description = repo_details.get('description', 'No description provided.')
    url = repo_details.get('url', '')
    homepage = repo_details.get('homepageUrl', '')
    created = repo_details.get('createdAt', '')
    updated = repo_details.get('updatedAt', '')
    stars = repo_details.get('stargazerCount', 0)
    forks = repo_details.get('forkCount', 0)
    is_archived = repo_details.get('isArchived', False)
    is_fork = repo_details.get('isFork', False)
    language = repo_details.get('primaryLanguage', {}).get('name', 'Unknown') if repo_details.get('primaryLanguage') else 'Unknown'
    languages = repo_details.get('languages', [])
    topics = repo_details.get('repositoryTopics', [])
    license_info = repo_details.get('licenseInfo', {})
    latest_release = repo_details.get('latestRelease')
    pages = repo_details.get('pages')
    readme_preview = repo_details.get('readmePreview', '')
    
    # Format dates
    try:
        created_date = datetime.fromisoformat(created.replace('Z', '+00:00')).strftime('%B %d, %Y')
        updated_date = datetime.fromisoformat(updated.replace('Z', '+00:00')).strftime('%B %d, %Y')
    except:
        created_date = created
        updated_date = updated
    
    md = f"""# {name}

{description}

"""
    
    # Add badges
    badges = []
    if stars > 0:
        badges.append(f"⭐ **{stars} stars**")
    if forks > 0:
        badges.append(f"🍴 **{forks} forks**")
    if is_archived:
        badges.append("📦 **Archived**")
    if is_fork:
        badges.append("🔱 **Fork**")
    
    if badges:
        md += " | ".join(badges) + "\n\n"
    
    # Quick Links section
    md += "## 🔗 Quick Links\n\n"
    md += f"- [📁 Repository]({url})\n"
    
    if homepage:
        md += f"- [🌐 Homepage]({homepage})\n"
    
    if pages and pages.get('html_url'):
        md += f"- [📄 GitHub Pages]({pages['html_url']})\n"
    
    if latest_release:
        release_url = latest_release.get('url', '')
        release_tag = latest_release.get('tagName', '')
        release_name = latest_release.get('name', release_tag)
        release_date = latest_release.get('publishedAt', '')
        try:
            release_date_fmt = datetime.fromisoformat(release_date.replace('Z', '+00:00')).strftime('%B %d, %Y')
        except:
            release_date_fmt = release_date
        md += f"- [🚀 Latest Release: {release_name}]({release_url}) - *{release_date_fmt}*\n"
    
    md += "\n"
    
    # Project Details section
    md += "## 📊 Project Details\n\n"
    md += f"- **Primary Language:** {language}\n"
    
    if languages and len(languages) > 0:
        # Languages structure: [{"size": ..., "node": {"name": "Python"}}, ...]
        lang_names = [lang.get('node', {}).get('name', '') for lang in languages if lang.get('node', {}).get('name')]
        if lang_names:
            # Sort by size (largest first) and take top 10
            langs_sorted = sorted(languages, key=lambda x: x.get('size', 0), reverse=True)[:10]
            lang_list = ", ".join([lang.get('node', {}).get('name', '') for lang in langs_sorted if lang.get('node', {}).get('name')])
            if lang_list:
                md += f"- **Languages Used:** {lang_list}\n"
            else:
                md += f"- **Languages Used:** Not specified\n"
        else:
            md += f"- **Languages Used:** Not specified\n"
    
    if license_info and license_info.get('name'):
        md += f"- **License:** {license_info['name']}\n"
    
    md += f"- **Created:** {created_date}\n"
    md += f"- **Last Updated:** {updated_date}\n"
    
    md += "\n"
    
    # Topics/Tags section
    if topics:
        md += "## 🏷️ Topics\n\n"
        topic_names = [topic.get('topic', {}).get('name', '') for topic in topics if topic.get('topic', {}).get('name')]
        md += ", ".join([f"`{topic}`" for topic in topic_names])
        md += "\n\n"
    
    # Description section with README preview
    if readme_preview and len(readme_preview) > len(description or ''):
        md += "## 📝 About\n\n"
        # Clean up the README preview (remove markdown headers, etc.)
        preview_lines = readme_preview.split('\n')
        clean_preview = []
        for line in preview_lines:
            if line.strip() and not line.startswith('#'):
                clean_preview.append(line)
            if len('\n'.join(clean_preview)) > 300:
                break
        
        if clean_preview:
            md += '\n'.join(clean_preview)
            if len('\n'.join(clean_preview)) < len(readme_preview):
                md += f"\n\n[Read more in the repository README]({url}#readme)"
            md += "\n\n"
    
    # Status section
    if is_archived or is_fork:
        md += "## ℹ️ Status\n\n"
        if is_archived:
            md += "⚠️ **This repository is archived** - It is read-only and no longer actively maintained.\n\n"
        if is_fork:
            md += "🔱 **This is a fork** - See the original repository for the upstream project.\n\n"
    
    # Footer
    md += "---\n\n"
    md += f"*Visit the [repository]({url}) for more information, code, and documentation.*\n"
    
    return md

# Main execution
print("Loading repositories list...")
with open('repos.json', 'r') as f:
    repos = json.load(f)

# Filter public repos
public_repos = [r for r in repos if not r.get('isPrivate', False)]
print(f"Found {len(public_repos)} public repositories")

# Process each repository
for i, repo in enumerate(public_repos, 1):
    repo_name = repo['nameWithOwner']
    print(f"\n[{i}/{len(public_repos)}] Processing {repo_name}...")
    
    # Get detailed info
    details = get_repo_details(repo_name)
    
    # Generate markdown
    if details:
        md_content = generate_enhanced_markdown(details)
        
        # Write to file
        filename = f"docs/{repo['name']}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"  ✓ Updated {filename}")
    else:
        print(f"  ✗ Failed to fetch details for {repo_name}")

print("\n✅ All project pages enhanced!")
