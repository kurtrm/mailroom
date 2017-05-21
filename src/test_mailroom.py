"""Test our creat_report functions."""


import pytest


# In the create_report function, we don't want to test what is being printed.
# We want to test the values that are returning


# Verify we are getting the name in the dictionary
# Get correct sums for each value in the dictionary
# Get correct length fo each dict_value
# Get correct avg for our values
# Get cor
PARAMS_TABLE = [
    ({'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]},
        ['Garth Brooks, 1, 1, 1',
        'Sam Wippy, 100000, 1, 100000',
        'Willy Wonka, 39, 3, 13']
        ),
    ({'Jarbo': [10, 1, 5, 115, 100, 20, 100000], 'Dick V. Dyke': [0]},
        ['Dick V. Dyke, 0, 1, 0',
        'Jarbo, 100251, 7, 14321']
        ),
    ({'Julia Roberts': [100000, 120, 15403]},
        ['Julia Roberts, 115523, 3, 38507']
        ),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_create_report(l, result):
    """Test the create report function."""
    from report import create_report
    assert create_report(l) == result
