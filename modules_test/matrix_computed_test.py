import math
from parameterized import parameterized, parameterized_class
import unittest

from ..packages.matrix_pkg import matrix, matrix_computed



# Computed Matrix Segment - Construction Test Cases ###########################

class ComputedMatrixSegmentConstructionTestCase(unittest.TestCase):
    @parameterized.expand([
        (-100, 0, 1),
        (-10, 0, 1),
        (-1, 0, 1),
        (0, 0, 1),
    ])
    def test_construction_invalid_length(self, length: int, index: int, value: int):
        def act():
            result: matrix.IMatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

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
            result: matrix.IMatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

        self.assertRaises(matrix.ArgumentException, act)

    @parameterized.expand([
        (1, 0, 1),
        (10, 0, 1),
        (100, 0, 1),
    ])
    def test_construction_valid(self, length: int, index: int, value: int):
        result: matrix.IMatrixSegment = matrix_computed.ComputedMatrixSegment( length, index, value)

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
        self.testSubject: matrix.IMatrixSegment = matrix_computed.ComputedMatrixSegment(
            self.segment_length,
            self.segment_index,
            self.segment_value)

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



# Computed Identity Matrix - Construction Test Cases ##########################

class ComputedIdentityMatrixConstructionTestCase(unittest.TestCase):
    @parameterized.expand([
        (-10,),
        (-1,),
        (0,),
    ])
    def test_construction_invalid_demensions(self, n: int):
        def act() -> None:
            result: matrix.IMatrix = matrix_computed.ComputedIdentityMatrix(n, 1)

        self.assertRaises(matrix.ArgumentException, act)

    @parameterized.expand([
        (1,42),
        (2,42),
        (4,42),
    ])
    def test_construction_valid_parameters(self, n: int, v: int):
        result: matrix.IMatrix = matrix_computed.ComputedIdentityMatrix(n, v)

        self.assertEqual(n, result.get_rows())
        self.assertEqual(n, result.get_columns())

        self.assertEqual(v, result.get_element(0, 0))



# Computed Identity Matrix - Test Cases #######################################

@parameterized_class(('matrix_demension', 'matrix_value'), [
    (1, 42),
    (2, 42),
    (4, 42),
    (16, 42),
])
class ComputedIdentityMatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.test_subject: matrix.IMatrix = matrix_computed.ComputedIdentityMatrix(
            self.matrix_demension,
            self.matrix_value)

    def test_get_rows(self):
        result: int = self.test_subject.get_rows()

        self.assertEqual(self.matrix_demension, result)

    def test_get_columns(self):
        result: int = self.test_subject.get_columns()

        self.assertEqual(self.matrix_demension, result)

    @parameterized.expand([
        (0,),
        (1,),
    ])
    def test_get_element(self, offset: int):
        if offset < self.matrix_demension:
            expected: int = 0

            if offset == 0:
                expected = self.matrix_value

            result1: int = self.test_subject.get_element(0, offset)
            result2: int = self.test_subject.get_element(offset, 0)

            self.assertEqual(expected, result1)
            self.assertEqual(expected, result2)

        else:
            self.skipTest(f"Matrix is too small for this test.")

    @parameterized.expand([
        (-10,),
        (-1,),
        (0,),
        (1,),
        (10,),
    ])
    def test_get_element_out_of_bounds(self, offset: int):
        i: int = offset

        if 0 <= i:
            i += self.matrix_demension

        def act1():
            result: int = self.test_subject.get_element(i, 0)

        def act2():
            result: int = self.test_subject.get_element(0, i)

        self.assertRaises(IndexError, act1)
        self.assertRaises(IndexError, act2)

    def test_set_element(self):
        def act():
            self.test_subject.set_element(0, 0, 1)

        self.assertRaises(matrix_computed.ComputedException, act)

    # TODO: Implement tests for get_row and get_column.



# Main module #################################################################

if __name__ == '__main__':
    unittest.main()
