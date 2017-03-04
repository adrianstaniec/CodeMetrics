from codemetrics.engine import gather_info

import pandas as pd

# TODO: make pass
def test_empty_projects():
    df, cnt = gather_info('stimuli/fake_codebase/not_empty_dir/empty_dir')
    assert df.empty
    assert cnt == 0

    df, cnt = gather_info('stimuli/fake_codebase/not_empty_dir/empty_file.txt')
    edf = pd.DataFrame(index=('txt',), data={'Files': 1, 'Lines': 0})
    assert (edf == df).all().all()
    assert cnt == 0

    df, cnt = gather_info('stimul/fake_codebase/not_empty_dir/empty_line.txt')
    edf = pd.DataFrame(index=('txt',), data={'Files': 1, 'Lines': 0})
    assert (edf == df).all().all()
    assert cnt == 0

    df, cnt = gather_info('stimul/fake_codebase/not_empty_dir/single_line.txt')
    edf = pd.DataFrame(index=('txt',), data={'Files': 1, 'Lines': 1})
    assert (edf == df).all().all()
    assert cnt == 0

    df, cnt = gather_info('stimul/fake_codebase/not_empty_dir/four_lines_two_empty.txt')
    edf = pd.DataFrame(index=('txt',), data={'Files': 1, 'Lines': 2})
    assert (edf == df).all().all()
    assert cnt == 0


# TODO: add more tests pass
