#!/usr/bin/env python3
"""
Regenerate the LeetCode problem list in README.md.

Usage:
  python3 regen_readme.py --branch main           # write changes (default: master)
  python3 regen_readme.py --branch main --dry-run # only print what would change
"""
import os, re, argparse

OWNER = "HetK2004"
REPO = "LeetCode"

start_marker = "<!---LeetCode Topics Start-->"
end_marker   = "<!---LeetCode Topics End-->"

parser = argparse.ArgumentParser()
parser.add_argument("--branch", default="master", help="Branch used in links (default: master). Use 'main' if your repo default is main.")
parser.add_argument("--dry-run", action="store_true", help="Don't write README.md; just print summary and preview.")
args = parser.parse_args()

# Collect problem folders that match pattern '0001-name'
dirs = [d for d in os.listdir(".") if os.path.isdir(d) and re.match(r"^\d{4}-", d)]
dirs.sort()

links = "\n".join(f"- [{d}](https://github.com/{OWNER}/{REPO}/tree/{args.branch}/{d})" for d in dirs)
block = f"{start_marker}\n\n{links}\n\n{end_marker}"

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

if start_marker in readme and end_marker in readme:
    head, rest = readme.split(start_marker, 1)
    _, tail = rest.split(end_marker, 1)
    new_readme = head + block + tail
    mode = "replaced existing markers"
else:
    new_readme = readme + "\n\n" + block + "\n"
    mode = "appended block (markers were missing)"

print(f"Found {len(dirs)} problem folders. Will {mode} in {readme_path}.\n")
if args.dry_run:
    # show a short preview
    preview_lines = block.splitlines()[:40]
    print("Preview of inserted block:\n")
    print("\n".join(preview_lines))
    print("\nDry-run: no file was modified.")
else:
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)
    print(f"README.md updated. Inserted {len(dirs)} links between markers.")
