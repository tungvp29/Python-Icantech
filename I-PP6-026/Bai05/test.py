import pytest 

def sum(a, b):
    return a - b

def test_sum():
    assert sum(2, 3) == 5


if __name__ == "__main__":
    test_sum()
    print("All tests passed.")
