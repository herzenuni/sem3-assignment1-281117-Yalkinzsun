from main import summator
import pytest


@pytest.mark.parametrize("a, result"[('123', 6), ('100500', 6), ('-777, ValueError')])
def testing_summator_v1(a, result):
    assert summator(a) == result