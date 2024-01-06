from matrix import get_number_of_columns, create_matrix, display_matrix

def transpose(matrix):
    ColumnsNumber = get_number_of_columns(matrix)
    Transpose = [[] for _ in range(ColumnsNumber)]    
    for MatrixRow in matrix:
        NumberColumn = 0
        for TransposeRow in Transpose:
            TransposeRow.append(MatrixRow[NumberColumn])
            NumberColumn += 1
    return Transpose

RowsNumber = int(input("Enter the number of rows: "))
ColumnsNumber = int(input("Enter the number of columns: "))
print()
Matrix = create_matrix(RowsNumber, ColumnsNumber)
print("\n\nthe matrix")
display_matrix(Matrix)
TransposeMatrix = transpose(Matrix)
print("\n\ntranspose of the matrix")
display_matrix(TransposeMatrix)
