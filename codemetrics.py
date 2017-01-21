"""
CodeMetrics - python script summarizing source code base
"""

import os           # for file access
import sys          # for command line arguments
import pandas as pd # for command line arguments

def scan_file(filepath):
    """Analyzes a single file's name and content"""
    dummy, ext = os.path.splitext(filepath)
    lncnt = 0
    with open(filepath) as filelines:
        for line in filelines:
            line = line.rstrip()
            if line != "":
                lncnt += 1
    return ext, lncnt

def main():
    """Main function"""
    if len(sys.argv) == 2:
        origin = sys.argv[1]
    else:
        origin = os.path.abspath('.')

    file_types = pd.Series(dtype='int64', name='Files')
    code_lines = pd.Series(dtype='int64', name='Lines')
    summary = pd.concat([file_types, code_lines], axis=1)

    for root, dummy, files in os.walk(origin):
        for filename in files:
            ext, lncnt = scan_file(os.path.join(root, filename))
            try:
                summary.loc[ext] += 1, lncnt
            except KeyError:
                summary.loc[ext] = 1, lncnt

    summary = summary.sort_values('Files', ascending=False)

    print("")
    print("Summary:")
    print(summary.head(20))

main()
