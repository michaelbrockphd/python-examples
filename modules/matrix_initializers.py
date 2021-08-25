from matrix import IMatrix



class IMatrixInitializer:
    """
    Interface describing all methods an initializer must implement.
    """

    def initialize_as_identity(self, m: IMatrix, v: int) -> None:
        pass

    def initialize_as_sequential(self, m: IMatrix) -> None:
        pass



class ConcreteMatrixInitializer(IMatrixInitializer):
    """
    Initializer for concrete matrixes.
    """

    def initialize_as_identity(self, m: IMatrix, v: int) -> None:
        num_rows: int = m.get_rows()

        i: int = 0

        while i < num_rows:
            m.set_element(i, i, v)

            i += 1
    
    def initialize_as_sequential(self, m: IMatrix) -> None:
        num_rows: int = m.get_rows()
        num_cols: int = m.get_columns()

        v: int = 0
        r: int = 0
        c: int = 0

        while r < num_rows:
            c = 0

            while c < num_cols:
                m.set_element(r, c, v)

                v += 1
                c += 1

            r += 1
