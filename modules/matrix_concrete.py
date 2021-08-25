from matrix import ArgumentException, Matrix, MatrixSegment



class CreateMatrixSegment:
    """
    Matrix segment implementation backed by an array.
    """

    # A matrix segment represents a single row or column yet provides a uniform interface for access and manipulation.

    def get_length(self) -> int:
        """Get the length of the segment."""
        pass

    def get_element(self, i: int) -> int:
        """Get the value at the specified index."""
        pass

    def set_element(self, i: int, v: int):
        """Set the value at the specified index."""
        pass



class LinearMatrix:
    """
    Array backed implementation of a matrix.  Should be used via an adapter to
    ease readibility and simplify code maintenance.
    """

    pass



class RowAlignedMatrix:
    """
    Adapter providing a row-aligned matrix.
    """

    def get_rows(self) -> int:
        """Get the number of rows in the matrix."""
        pass

    def get_columns(self) -> int:
        """Get the number of columns in the matrix."""
        pass

    def get_element(self, r: int, c: int) -> int:
        """Get the value of the specified element."""
        pass

    def set_element(self, r: int, c: int, v: int):
        """Set the value of the specified element."""
        pass

    def get_row(self, r: int) -> MatrixSegment:
        """Get the whole matrix row."""
        pass

    def get_column(self, c: int) -> MatrixSegment:
        """Get the whole matrix column."""
        pass



class ColumnAlignedMatrix:
    """
    Adapter providing a column-aligned matrix.
    """

    def get_rows(self) -> int:
        """Get the number of rows in the matrix."""
        pass

    def get_columns(self) -> int:
        """Get the number of columns in the matrix."""
        pass

    def get_element(self, r: int, c: int) -> int:
        """Get the value of the specified element."""
        pass

    def set_element(self, r: int, c: int, v: int):
        """Set the value of the specified element."""
        pass

    def get_row(self, r: int) -> MatrixSegment:
        """Get the whole matrix row."""
        pass

    def get_column(self, c: int) -> MatrixSegment:
        """Get the whole matrix column."""
        pass
