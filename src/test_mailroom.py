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
        ['Sam Wippy: 1 donation(s) totalling $100000. Average: $100000.',
        'Willy Wonka: 3 donation(s) totalling $39. Average: $13.',
        'Garth Brooks: 1 donation(s) totalling $1. Average: $1.']
        ),
    ({'Jarbo': [10, 1, 5, 115, 100, 20, 100000], 'Dick V. Dyke': [0]},
        ['Jarbo: 7 donation(s) totalling $100251. Average: $14321.',
        'Dick V. Dyke: 1 donation(s) totalling $0. Average: $0.']
        ),
    ({'Julia Roberts': [100000, 120, 15403]},
        ['Julia Roberts: 3 donation(s) totalling $115523. Average: $38507.']
        ),
    ({}, 'There are no donors at this time.'),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_create_report(l, result):
    """Test the create report function."""
    from Report import create_report
    assert create_report(l) == result