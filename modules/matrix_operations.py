from matrix import IMatrix



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

    pass
