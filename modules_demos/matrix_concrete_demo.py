import sys
sys.path.append( '../packages' )

from matrix import matrix, matrix_concrete, matrix_initializers, matrix_operations, matrix_computed



def print_matrix(m: matrix.IMatrix):
    rows: int = m.get_rows()

    i: int = 0

    while i < rows:
        row: matrix.IMatrixSegment = m.get_row(i)

        print(row)

        i += 1



def demonstrate_identity(m: matrix.IMatrix, initializer: matrix_initializers.IMatrixInitializer):
    initializer.initialize_as_identity(m, 42)

    print_matrix(m)

    print(f"\n")



def demonstrate_sequential(m: matrix.IMatrix, initializer: matrix_initializers.IMatrixInitializer):
    initializer.initialize_as_sequential(m)

    print_matrix(m)

    print(f"\n")



def demonstrate_row_aligned(r: int, c: int, initializer: matrix_initializers.IMatrixInitializer):
    print(f"Row Aligned :: Identity\n")

    matrix: matrix.IMatrix = matrix_concrete.RowAlignedMatrix(r, c)

    demonstrate_identity(matrix, initializer)

    print(f"Row Aligned :: Sequential\n")

    matrix = matrix_concrete.RowAlignedMatrix(r, c)

    demonstrate_sequential(matrix, initializer)



def demonstrate_column_aligned(r: int, c: int, initializer: matrix_initializers.IMatrixInitializer):
    print(f"Column Aligned :: Identity\n")

    matrix: matrix.IMatrix = matrix_concrete.ColumnAlignedMatrix(r, c)

    demonstrate_identity(matrix, initializer)

    print(f"Column Aligned :: Sequential\n")

    matrix = matrix_concrete.ColumnAlignedMatrix(r, c)

    demonstrate_sequential(matrix, initializer)

def demonstrate_multiplication(r: int, c: int, initializer: matrix_initializers.IMatrixInitializer):
    print(f"\nMultiplication Demo 1 :: Both Concrete\n")

    print(f"\nMatrix A :: Row Aligned\n")

    matrix_a: matrix.IMatrix = matrix_concrete.RowAlignedMatrix(r, c)

    initializer.initialize_as_sequential(matrix_a)

    print_matrix(matrix_a)

    print(f"\nMatrix B :: Column Aligned\n")

    matrix_b: matrix.IMatrix = matrix_concrete.ColumnAlignedMatrix(r, c)

    initializer.initialize_as_identity(matrix_b, 2)

    print_matrix(matrix_b)

    print(f"\nMatrix C :: Result of A * B\n")

    operations: matrix_operations.IMatrixOperations = matrix_operations.UniversalMatrixOperations()

    matrix_c: matrix.IMatrix = operations.multiply(matrix_a, matrix_b)

    print_matrix(matrix_c)

def demonstrate_multiplication_with_computed(r: int, c: int, initializer: matrix_initializers.IMatrixInitializer):
    print(f"\nMultiplication Demo 2 :: Concrete with Computed\n")

    print(f"\nMatrix A :: Row Aligned\n")

    matrix_a: matrix.IMatrix = matrix_concrete.RowAlignedMatrix(r, c)

    initializer.initialize_as_sequential(matrix_a)

    print_matrix(matrix_a)

    print(f"\nMatrix B :: Computed\n")

    matrix_b: matrix.IMatrix = matrix_computed.ComputedIdentityMatrix(r, 2)

    print_matrix(matrix_b)

    print(f"\nMatrix C :: Result of A * B\n")

    operations: matrix_operations.IMatrixOperations = matrix_operations.UniversalMatrixOperations()

    matrix_c: matrix.IMatrix = operations.multiply(matrix_a, matrix_b)

    print_matrix(matrix_c)



if __name__ == '__main__':
    initializer = matrix_initializers.ConcreteMatrixInitializer()

    demonstrate_row_aligned(10, 10, initializer)

    demonstrate_column_aligned(10, 10, initializer)

    demonstrate_multiplication(10, 10, initializer)

    demonstrate_multiplication_with_computed(10, 10, initializer)
