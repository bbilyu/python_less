import unittest
from matrix import Matrix


class MatrixTests(unittest.TestCase):

    def test_str(self):
        m = Matrix([[1, 2], [3, 4]])
        self.assertEqual(m.__str__(), '1\t2\n3\t4')

    def test_eq(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        self.assertTrue(m1 == m2)

    def test_add(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m3 = m1+m2
        self.assertEqual(m3.__str__(), '6\t8\n10\t12')

    def test_mul(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        m4 = m1*m2
        self.assertEqual(m4.__str__(), '19\t22\n43\t50')

    def test_add_invalid_size(self):
        m1 = Matrix([[1, 2], [3, 4]])
        m5 = Matrix([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            m1+m5


if __name__ == '__main__':
    unittest.main()
