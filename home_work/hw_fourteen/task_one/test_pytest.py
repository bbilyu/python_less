import pytest
from matrix import Matrix
def test_str():
    m = Matrix([[1, 2], [3, 4]])
    assert m.__str__() == '1\t2\n3\t4'

def test_eq():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 2], [3, 4]])
    assert m1 == m2

def test_add():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = m1+m2
    assert m3.__str__() == '6\t8\n10\t12'

def test_mul():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m4 = m1*m2
    assert m4.__str__() == '19\t22\n43\t50'

def test_add_invalid_size():
    m1 = Matrix([[1, 2], [3, 4]])
    m5 = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        m1 + m5

if __name__ == '__main__':
    pytest.main()