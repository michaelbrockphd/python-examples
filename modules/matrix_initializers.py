from matrix import IMatrix



class IMatrixInitializer:
    """
    Interface describing all methods an initializer must implement.
    """

    def initialize_as_identity(m: IMatrix, v: int) -> None:
        pass

    def initialize_as_sequential(m: IMatrix) -> None:
        pass



class ConcreteMatrixInitializer(IMatrixInitializer):
    """
    Initializer for concrete matrixes.
    """

    pass
