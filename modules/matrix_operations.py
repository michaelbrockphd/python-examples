from matrix import IMatrixSegment, IMatrix
from matrix_concrete import RowAlignedMatrix



class IMatrixOperations:
    """
    List of methods a helper class must implement to support matrix operations.
    """

    def multiply(a: IMatrix, b: IMatrix) -> IMatrix:
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
        numR: int = a.get_rows()
        numC: int = b.get_columns()

        rtn: IMatrix = RowAlignedMatrix(numR, numC)

        idxR: int = 0
        idxC: int = 0

        curR: IMatrixSegment = None
        curC: IMatrixSegment = None

        while idxR < numR:
            curR = a.get_row(idxR)
            idxC = 0

            while idxC < numC:
                curC = b.get_column(idxC)

                rtn.set_element(idxR, idxC, self.multiply_segements(curR, curC))

                idxC += 1

            idxR += 1

        return rtn
