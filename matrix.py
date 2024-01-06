def create_matrix(row_number, column_number):
    Matrix = [[] for _ in range(row_number)]
    RowNumber = 1
    for Row in Matrix:
        print("Row " + str(RowNumber))
        ColumnNumber = 1
        for Column in range(column_number):
            ColumnValue = int(input("\tEnter value in column " + str(ColumnNumber) + ": "))
            Row.append(ColumnValue)
            ColumnNumber += 1
        RowNumber += 1
        
    return Matrix

Matrix = create_matrix(3, 3)
print(Matrix)
