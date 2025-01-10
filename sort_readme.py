import re

def sort_toc(readme_path):
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    toc_start = None
    toc_end = None
    toc_pattern = re.compile(r'- \[(\d+)\. .+\]\(.+\)')

    for i, line in enumerate(lines):
        if toc_pattern.match(line):
            if toc_start is None:
                toc_start = i
            toc_end = i

    if toc_start is not None and toc_end is not None:
        toc_lines = lines[toc_start:toc_end + 1]
        toc_lines.sort(key=lambda x: int(toc_pattern.match(x).group(1)))
        lines = lines[:toc_start] + toc_lines + lines[toc_end + 1:]

    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    sort_toc('README.md')