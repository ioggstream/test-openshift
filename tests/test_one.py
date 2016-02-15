from nose.tools import * 
def test_sample():
    for i in range(5):
        yield assert_true, i
