import math
from parameterized import parameterized
import unittest

import sys

from parameterized.parameterized import param, parameterized_class
sys.path.append( '../modules' )

import matrix
import matrix_computed



# Computed Matrix Segment - Construction Test Cases ###########################

class ComputedMatrixSegmentConstructionTestCase(unittest.TestCase):
    def setup(self):
        pass

    @parameterized.expand([
        (-100, 0, 1),
        (-10, 0, 1),
        (-1, 0, 1),
        (0, 0, 1),
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
        (10, 100, 1),
    ])
    def test_construction_invalid_index(self, length: int, index: int, value: int):
        def act():
            result: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertRaises(matrix.ArgumentException, act)

    @parameterized.expand([
        (1, 0, 1),
        (10, 0, 1),
        (100, 0, 1),
    ])
    def test_construction_valid(self, length: int, index: int, value: int):
        result: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertEqual(length, result.get_length())



# Computed Matrix Segment - Test Cases ########################################

@parameterized_class(('segment_length', 'segment_index', 'segment_value'), [
    (1, 0, 42),
    (2, 1, 42),
    (4, 3, 42),
    (10, 4, 42),
    (100, 5, 42),
])
class ComputedMatrixSegmentTestCase(unittest.TestCase):
    def setUp(self):
        self.segment_length = 10
        self.segment_index = 1
        self.segment_value = 42

        self.testSubject: matrix.MatrixSegment = matrix_computed.ComputedMatrixSegment(self.segment_length, self.segment_index, self.segment_value)

    def test_get_length(self):
        self.assertEqual(self.segment_length, self.testSubject.get_length())

    @parameterized.expand([
        (0.0,),
        (0.5,),
        (1.0,),
    ])
    def test_get_element(self, scale: int):
        i: int = math.floor(self.segment_length * scale)

        if i == self.segment_length:
            i -= 1

        result = self.testSubject.get_element(i)

        self.assertIsNotNone(result)

    def test_get_element_at_index(self):
        result: int = self.testSubject.get_element(self.segment_index)

        self.assertEqual(self.segment_value, result)

    @parameterized.expand([
        (-10,),
        (-1,),
        (0,),
        (1,),
        (10,),
    ])
    def test_get_element_outofbounds(self, offset: int):
        i: int = 0

        if offset < 0:
            i = offset
        else:
            i = self.segment_length + offset

        def act():
            result = self.testSubject.get_element(i)

        self.assertRaises(IndexError, act)

    def test_set_element(self):
        def act():
            self.testSubject.set_element(0, 24)

        self.assertRaises(matrix_computed.ComputedException, act)



# Main module #################################################################

if __name__ == '__main__':
    unittest.main()
