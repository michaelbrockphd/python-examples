from .matrix import IMatrix, IMatrixSegment



class ConcreteMatrixSegment(IMatrixSegment):
    """
    Matrix segment implementation backed by an array.
    """

    # A matrix segment represents a single row or column yet provides a uniform interface for access and manipulation.

    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return f"{self.elements}"

    def get_length(self) -> int:
        """Get the length of the segment."""
        return len(self.elements)

    def get_element(self, i: int) -> int:
        """Get the value at the specified index."""
        length: int = len(self.elements)

        if not(0 <= i < length):
            raise IndexError(f"Index {i} out of bounds!")

        return self.elements[i]

    def set_element(self, i: int, v: int):
        """Set the value at the specified index."""
        length: int = len(self.elements)

        if not(0 <= i < length):
            raise IndexError(f"Index {i} out of bounds!")
        
        self.elements[i] = v



class LinearMatrix:
    """
    Array backed implementation of a matrix.  Should be used via an adapter to
    ease readibility and simplify code maintenance.
    """

    def __init__(self, count: int, size: int):
        self.count: int = count
        self.size: int = size

        self.elements = [0] * (count * size)

    def get_count(self) -> int:
        return self.count

    def get_size(self) -> int:
        return self.size

    def read_element(self, c: int, offset: int) -> int:
        # Make it the responsibility of the adapters to validate the input
        # parameters.

        i: int = (c * self.size) + offset

        return self.elements[i]

    def write_element(self, c: int, offset: int, v: int):
        # Make it the responsibility of the adapters to validate the input
        # parameters.

        i: int = (c * self.size) + offset

        self.elements[i] = v

    def get_section(self, n: int):
        # Make it the responsibility of the adapters to validate the input
        # parameters.

        offset: int = n * self.size

        sec = self.elements[offset:offset + self.size]

        return sec

    def get_cross_section(self, n):
        # Make it the responsibility of the adapters to validate the input
        # parameters.

        sec = [0] * self.count

        i: int = 0

        offset: int = n

        while i < self.count:
            sec[i] = self.elements[offset]

            i += 1

            offset += self.size

        return sec



class RowAlignedMatrix(IMatrix):
    """
    Adapter providing a row-aligned matrix.
    """

    def __init__(self, rows: int, columns: int):
        self.mtx = LinearMatrix(rows, columns)

    def get_rows(self) -> int:
        """Get the number of rows in the matrix."""
        return self.mtx.get_count()

    def get_columns(self) -> int:
        """Get the number of columns in the matrix."""
        return self.mtx.get_size()

    def get_element(self, r: int, c: int) -> int:
        """Get the value of the specified element."""
        return self.mtx.read_element(r, c)

    def set_element(self, r: int, c: int, v: int):
        """Set the value of the specified element."""
        self.mtx.write_element(r, c, v)

    def get_row(self, r: int) -> IMatrixSegment:
        """Get the whole matrix row."""
        sec = self.mtx.get_section(r)

        row: IMatrixSegment = ConcreteMatrixSegment(sec)

        return row

    def get_column(self, c: int) -> IMatrixSegment:
        """Get the whole matrix column."""
        sec = self.mtx.get_cross_section(c)

        col: IMatrixSegment = ConcreteMatrixSegment(sec)

        return col



class ColumnAlignedMatrix(IMatrix):
    """
    Adapter providing a column-aligned matrix.
    """

    def __init__(self, rows: int, columns: int):
        self.mtx = LinearMatrix(columns, rows)

    def get_rows(self) -> int:
        """Get the number of rows in the matrix."""
        return self.mtx.get_size()

    def get_columns(self) -> int:
        """Get the number of columns in the matrix."""
        return self.mtx.get_count()

    def get_element(self, r: int, c: int) -> int:
        """Get the value of the specified element."""
        return self.mtx.read_element(c, r)

    def set_element(self, r: int, c: int, v: int):
        """Set the value of the specified element."""
        self.mtx.write_element(c, r, v)

    def get_row(self, r: int) -> IMatrixSegment:
        """Get the whole matrix row."""
        sec = self.mtx.get_cross_section(r)

        row: IMatrixSegment = ConcreteMatrixSegment(sec)

        return row

    def get_column(self, c: int) -> IMatrixSegment:
        """Get the whole matrix column."""
        sec = self.mtx.get_section(c)

        col: IMatrixSegment = ConcreteMatrixSegment(sec)

        return col
