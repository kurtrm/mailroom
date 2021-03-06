"""Test our creat_report functions."""
import pytest


PARAMS_TABLE = [
    ({'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]},
        [('Sam Wippy', 100000, 1, 100000),
            ('Willy Wonka', 39, 3, 13),
            ('Garth Brooks', 1, 1, 1)]
     ),
    ({'Jarbo': [10, 1, 5, 115, 100, 20, 100000], 'Dick V. Dyke': [0]},
        [('Jarbo', 100251, 7, 14321),
            ('Dick V. Dyke', 0, 1, 0)]
     ),
    ({'Julia Roberts': [100000, 120, 15403]},
        [('Julia Roberts', 115523, 3, 38507)]
     ),
]


list_result = 'TEST NOTE'


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_create_report(l, result):
    """Test the create report function."""
    from mailroom_tests import create_report
    assert create_report(l) == result


def test_add_new_or_update_donor_info_success():
    """Test parts of this function."""
    from mailroom_tests import add_new_or_update_donor_info
    assert add_new_or_update_donor_info("Jacob Brinkley", 200) == list_result


def test_add_new_or_update_donor_info_fail():
    """Test parts of this function."""
    from mailroom_tests import add_new_or_update_donor_info
    assert add_new_or_update_donor_info("jeepers", "Cool Whip") is None


def test_add_new_or_update_donor_info_negative_number():
    """Ensure we can't pass in a negative number."""
    from mailroom_tests import add_new_or_update_donor_info
    assert add_new_or_update_donor_info("Willy Boo", -200)
