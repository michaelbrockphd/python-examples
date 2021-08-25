import sys
sys.path.append( '../modules' )

import matrix
import matrix_concrete
import matrix_initializers



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



if __name__ == '__main__':
    initializer = matrix_initializers.ConcreteMatrixInitializer()

    demonstrate_row_aligned(10, 10, initializer)

    demonstrate_column_aligned(10, 10, initializer)
