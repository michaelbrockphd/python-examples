from matrix import ArgumentException, MatrixSegment

class ComputedError(Exception):
    pass

class ComputedMatrixSegment(MatrixSegment):
    """A computed matrix segment to save memory."""
    def __init__(self, l: int, i: int, v: int):
        # While treated as an interface, it is always best practice to call the
        # parent constructor - no exceptions.
        super().__init__()

        if l < 1:
            raise ArgumentException("Length must be at least 1.")

        if i < 0 or l <= i:
            raise ArgumentException(f"Index must be at least 0 and less than {l}")

        self.length: int = l
        self.index: int = i
        self.value: int = v
    
    def get_length(self) -> int:
        return self.length

    def get_element(self, i: int) -> int:
        if i < 0 or self.length <= i:
            raise IndexError(f"{i} must be between 0 and {self.length}, inclusive.")

        rtn: int = 0

        if i == self.index:
            rtn = self.value

        return rtn

    def set_element(self, i: int, v: int):
        raise ComputedError( "Computed segments are not writable." )
