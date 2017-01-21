"""
CodeMetrics - python script summarizing source code base
"""

import os           # for file access
import sys          # for command line arguments
import pandas as pd # for command line arguments

def scan_file(arg):
    """Analyzes a single file's name and content"""
    dummy, ext = os.path.splitext(arg)
    return ext

def main():
    """Main function"""
    if len(sys.argv) == 2:
        origin = sys.argv[1]
    else:
        origin = os.path.abspath('.')

    ext_index = pd.Series(dtype='int64')

    for dummy, dummy, filenames in os.walk(origin):
        for filename in filenames:
            ext = scan_file(filename)
            try:
                ext_index[ext] += 1
            except KeyError:
                ext_index[ext] = 1

    ext_index = ext_index.sort_values(ascending=False)

    print("File count results:")
    print(ext_index.head(n=20))

main()
