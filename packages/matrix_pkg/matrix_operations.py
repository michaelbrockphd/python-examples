from .matrix import IMatrixSegment, IMatrix
from .matrix_concrete import RowAlignedMatrix



class IMatrixOperations:
    """
    List of methods a helper class must implement to support matrix operations.
    """

    def multiply(self, a: IMatrix, b: IMatrix) -> IMatrix:
        """
        Multiply Matrix A with Matrix B.

        Every column of Matrix A is multiplied by every row in Matrix B.
        """
        pass



class UniversalMatrixOperations(IMatrixOperations):
    """
    Class that provides operations that can be applied to any matrix type.
    """

    def multiply_segements(self, a: IMatrixSegment, b: IMatrixSegment) -> int:
        rtn: int = 0

        l: int = a.get_length()
        i: int = 0

        while i < l:
            rtn += (a.get_element(i) * b.get_element(i))

            i += 1

        return rtn

    def multiply(self, a: IMatrix, b: IMatrix) -> IMatrix:
        num_r: int = a.get_rows()
        num_c: int = b.get_columns()

        rtn: IMatrix = RowAlignedMatrix(num_r, num_c)

        idx_r: int = 0
        idx_c: int = 0

        cur_r: IMatrixSegment = None
        cur_c: IMatrixSegment = None

        while idx_r < num_r:
            cur_r = a.get_row(idx_r)
            idx_c = 0

            while idx_c < num_c:
                cur_c = b.get_column(idx_c)

                rtn.set_element(idx_r, idx_c, self.multiply_segements(cur_r, cur_c))

                idx_c += 1

            idx_r += 1

        return rtn
