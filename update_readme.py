import os
import re
from sort_readme import sort_toc

def get_problem_folders():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    folders = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and re.match(r'^\d+\.', item):
            folders.append(item)
    return folders

def get_solution_file(folder_path):
    file_priority = [
        'main.go',
        'main.rs',
        'main.py',
        'main.cpp',
        'main.java',     
        'main.js',
        'main.ts',
        'main.rb',
    ]
    
    for file in file_priority:
        if os.path.exists(os.path.join(folder_path, file)):
            return file
    return 'main.go'  

def update_readme(readme_path=None):
    if readme_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        readme_path = os.path.join(script_dir, 'README.md')
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for README at: {readme_path}")
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found!")
        return
        
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not read {readme_path}")
        return

    parts = content.split('<!-- Start  -->')
    if len(parts) < 2:
        return
    
    before_content = parts[0] + '<!-- Start  -->\n\n'
    middle_parts = parts[1].split('<!-- End  -->')
    after_content = '\n<!-- End  -->' + middle_parts[1] if len(middle_parts) > 1 else '\n<!-- End  -->'

    folders = get_problem_folders()
    entries = []
    for folder in folders:
        encoded_path = folder.replace(' ', '%20')
        solution_file = get_solution_file(folder)
        entries.append(f"- [{folder}](./{encoded_path}/{solution_file})")

    sorted_entries = sorted(entries, key=lambda x: int(re.search(r'\[(\d+)\.', x).group(1)))
    
    new_content = (
        before_content +
        '\n'.join(sorted_entries) +
        '\n' +
        after_content
    )

    with open(readme_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
