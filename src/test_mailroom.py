
import pytest
# import os

TRI_SOURCE_LIST = [
    ('One night--it', ['was']),
    ('night--it was', ['on']),
    ('was on', ['the']),
    ('on the', ['twentieth']),
    ('the twentieth', ['of'])
]


# dirpath = os.path.dirname(os.path.abspath(__file__))
# source_file = os.path.join(dirpath, 'body_text.txt')

# import pdb; pdb.set_trace()

# @pytest.mark.parametrize('n, result', TRI_SOURCE_LIST)
def test_send_thank_you():
    from thank_you import send_thank_you
    assert send_thank_you() == result


# def test_trigrams_random_int():
#     from trigrams import trigrams_random_int
#     for n in range(1, 100):
#         assert trigrams_random_int(n) in range(n)
