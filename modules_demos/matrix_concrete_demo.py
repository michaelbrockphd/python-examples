import sys
sys.path.append( '../modules' )

import matrix
import matrix_concrete
import matrix_initializers
import matrix_operations
import matrix_computed



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

    matrixA: matrix.IMatrix = matrix_concrete.RowAlignedMatrix(r, c)

    initializer.initialize_as_sequential(matrixA)

    print_matrix(matrixA)

    print(f"\nMatrix B :: Column Aligned\n")

    matrixB: matrix.IMatrix = matrix_concrete.ColumnAlignedMatrix(r, c)

    initializer.initialize_as_identity(matrixB, 2)

    print_matrix(matrixB)

    print(f"\nMatrix C :: Result of A * B\n")

    operations: matrix_operations.IMatrixOperations = matrix_operations.UniversalMatrixOperations()

    matrixC: matrix.IMatrix = operations.multiply(matrixA, matrixB)

    print_matrix(matrixC)

def demonstrate_multiplication_with_computed(r: int, c: int, initializer: matrix_initializers.IMatrixInitializer):
    print(f"\nMultiplication Demo 2 :: Concrete with Computed\n")

    print(f"\nMatrix A :: Row Aligned\n")

    matrixA: matrix.IMatrix = matrix_concrete.RowAlignedMatrix(r, c)

    initializer.initialize_as_sequential(matrixA)

    print_matrix(matrixA)

    print(f"\nMatrix B :: Computed\n")

    matrixB: matrix.IMatrix = matrix_computed.ComputedIdentityMatrix(r, 2)

    print_matrix(matrixB)

    print(f"\nMatrix C :: Result of A * B\n")

    operations: matrix_operations.IMatrixOperations = matrix_operations.UniversalMatrixOperations()

    matrixC: matrix.IMatrix = operations.multiply(matrixA, matrixB)

    print_matrix(matrixC)



if __name__ == '__main__':
    initializer = matrix_initializers.ConcreteMatrixInitializer()

    demonstrate_row_aligned(10, 10, initializer)

    demonstrate_column_aligned(10, 10, initializer)

    demonstrate_multiplication(10, 10, initializer)

    demonstrate_multiplication_with_computed(10, 10, initializer)
