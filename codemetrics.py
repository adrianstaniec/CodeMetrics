"""
CodeMetrics - python script summarizing source code base
"""

import os           # for file access
import sys          # for command line arguments
import pandas as pd # for data storage and manipulation

def scan_file(filepath):
    """Analyzes a single file's name and content"""
    dummy, ext = os.path.splitext(filepath)
    lncnt = 0
    omitted = 0

    encodings = ['utf-8', None]
    for enc in encodings:
        try:
            with open(filepath, mode='r', encoding=enc) as filelines:
            # with open(filepath) as filelines:
                for line in filelines:
                    line = line.rstrip()
                    if line != "":
                        lncnt += 1
            break
        except UnicodeDecodeError:
            continue
    else:
        omitted = 1

    return ext, lncnt, omitted

def main():
    """Main function"""
    # Process command line arguments
    if len(sys.argv) == 2:
        origin = sys.argv[1]
    else:
        origin = os.path.abspath('.')

    # Prepare data structures
    file_types = pd.Series(dtype='int64', name='Files')
    code_lines = pd.Series(dtype='int64', name='Lines')
    summary = pd.concat([file_types, code_lines], axis=1)
    summary.index.name = "File type"
    omit_cnt = 0

    # Gather information
    for root, dummy, files in os.walk(origin):
        for filename in files:
            ext, lncnt, omitted = scan_file(os.path.join(root, filename))
            omit_cnt += omitted
            try:
                summary.loc[ext] += 1, lncnt
            except KeyError:
                summary.loc[ext] = 1, lncnt

    # Format data
    summary = summary.sort_values('Lines', ascending=False)
    summary = summary.sort_values('Files', ascending=False)

    # Print results
    print("")
    print("Summary:")
    print(summary.head(20))

    if omit_cnt > 0:
        print("")
        print("Lines in {0} files were not counted, due to decoding problems.".format(omit_cnt))

if __name__ == "__main__":
    main()