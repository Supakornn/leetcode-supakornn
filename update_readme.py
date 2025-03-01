import os
import re
from sort_readme import sort_toc

def get_problem_folders():
    folders = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and re.match(r'^\d+\.', item):
            folders.append(item)
    return folders

def update_readme():
    try:
        with open('README.md', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = """# LeetCode Solutions\n\n## 🌟 My Personal LeetCode Solutions\n\n- This repository is a collection of my personal LeetCode solutions.\n\n### 📚 Table of Contents\n\n"""

    folders = get_problem_folders()
    entries = []
    for folder in folders:
        entries.append(f"- [{folder}](/{folder}/main.go)")
    
    toc_pattern = re.compile(r'(### 📚 Table of Contents\n\n)((?:- \[.+?\]\(.+?\)\n)*)', re.MULTILINE)
    toc_match = toc_pattern.search(content)
    
    if toc_match:
        new_content = content[:toc_match.start(2)] + '\n'.join(entries) + '\n'
        if toc_match.end(2) < len(content):
            new_content += content[toc_match.end(2):]
    else:
        new_content = content + '\n'.join(entries) + '\n'

    with open('README.md', 'w') as f:
        f.write(new_content)
    
    sort_toc('README.md')

if __name__ == "__main__":
    update_readme()
