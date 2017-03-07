from codemetrics.engine import gather_info

import os
import pandas as pd
import pandas.util.testing as pdt

def test_empty_dir():
    df, cnt = gather_info('stimuli/subdirectories/empty_dir')
    assert df.empty
    assert cnt == 0

def test_empty_file():
    df, cnt = gather_info('tests/stimuli/subdirectories/single_empty_file')
    edf = pd.DataFrame(index=('.txt',), data={'Files': 1, 'Lines': 0})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 0

def test_single_empty_line():
    df, cnt = gather_info('tests/stimuli/subdirectories/single_empty_line')
    edf = pd.DataFrame(index=('.txt',), data={'Files': 1, 'Lines': 0})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 0

def test_single_nonempty_line():
    df, cnt = gather_info('tests/stimuli/subdirectories/single_nonempty_line')
    edf = pd.DataFrame(index=('.txt',), data={'Files': 1, 'Lines': 1})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 0

def test_four_lines_two_empty():
    df, cnt = gather_info('tests/stimuli/subdirectories/four_lines_two_empty')
    edf = pd.DataFrame(index=('.txt',), data={'Files': 1, 'Lines': 2})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 0

def test_two_empty_files():
    df, cnt = gather_info('tests/stimuli/subdirectories/two_empty_files')
    edf = pd.DataFrame(index=('.txt',), data={'Files': 2, 'Lines': 0})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 0

def test_one_nontext_files():
    df, cnt = gather_info('tests/stimuli/subdirectories/one_nontext_file')
    edf = pd.DataFrame(index=('.jpg',), data={'Files': 1, 'Lines': 0})
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 1

def test_subdirectories():
    df, cnt = gather_info('tests/stimuli/subdirectories')
    edf = pd.DataFrame(index=('.txt','.jpg'), data=[{'Files': 6, 'Lines': 3},
                                                    {'Files': 1, 'Lines': 0}])
    edf.index.name = 'File type'
    pdt.assert_frame_equal(df, edf)
    assert cnt == 1
