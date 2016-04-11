from nose.tools import * 
def test_sample():
    for i in range(1,6):
        yield assert_true, i

def test_python():
    from sys import version_info
    assert version_info < (3,0), "Python 3 is not supported."
