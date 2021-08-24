from parameterized import parameterized
import unittest

import sys

from parameterized.parameterized import param
sys.path.append( '../modules' )

import matrix
import matrix_computed

class ComputedMatrixSegmentConstructionTestCase(unittest.TestCase):
    def setup(self):
        pass

    @parameterized.expand([
        (-100, 0, 1),
        (-10, 0, 1),
        (-1, 0, 1),
        (0, 0, 1)
    ])
    def test_construction_invalid_length(self, length: int, index: int, value: int):
        def act():
            result: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertRaises(matrix.ArgumentException, act)

    @parameterized.expand([
        (10, -100, 1),
        (10, -10, 1),
        (10, -1, 1),
        (10, 11, 1),
        (10, 100, 1)
    ])
    def test_construction_invalid_index(self, length: int, index: int, value: int):
        def act():
            result: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertRaises(matrix.ArgumentException, act)

    @parameterized.expand([
        (1, 0, 1),
        (10, 0, 1),
        (100, 0, 1)
    ])
    def test_construction_valid(self, length: int, index: int, value: int):
        result: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertEqual(result.get_length(), length)

if __name__ == '__main__':
    unittest.main()
