from Cheetah.NameMapper import valueFromSearchList as VFSL
from constants import ITERATIONS


SL = [{'bar': 'wat'}]


def run():
    assert VFSL(SL, 'bar') == 'wat'
    [VFSL(SL, 'bar') for _ in range(ITERATIONS)]
