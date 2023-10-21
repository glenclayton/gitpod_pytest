import main
import numpy as np

def test_add():
    assert main.add(1,2) == 3

def test_concat():
    a = np.array([1,2])
    b = np.array([3,4])
    c = main.my_concat(a,b)
    assert c.size == 4

