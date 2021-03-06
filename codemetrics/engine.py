"""
Engine module for Code Metrics
"""

import os
import pandas as pd


def scan_file(file_path):
    """Analyzes a single file's name and content"""
    dummy, ext = os.path.splitext(file_path)
    lncnt = 0
    omitted = 0

    encodings = ['utf-8', None]
    for enc in encodings:
        try:
            with open(file_path, mode='r', encoding=enc) as filelines:
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


def gather_info(dir_path):
    """Crawl the directory for stats"""
    # Prepare data structures
    file_types = pd.Series(dtype='int64', name='Files')
    code_lines = pd.Series(dtype='int64', name='Lines')
    summary = pd.concat([file_types, code_lines], axis=1)
    summary.index.name = "File type"
    omit_cnt = 0

    # Gather information
    for root, dummy, files in os.walk(dir_path):
        for filename in files:
            ext, lncnt, omitted = scan_file(os.path.join(root, filename))
            omit_cnt += omitted
            ext = ext.lower()
            try:
                summary.loc[ext] += 1, lncnt
            except KeyError:
                summary.loc[ext] = 1, lncnt

    return summary, omit_cnt
