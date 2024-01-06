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

def get_number_of_columns(matrix):
    NumberOfColumns = len(matrix[0])
    return NumberOfColumns

def get_max_length_on_column(column_number, matrix):
    MaxLength = 1
    for Row in Matrix:
        LenghtOfColumn = len(str(Row[column_number]))
        if LenghtOfColumn > MaxLength:
            MaxLength = LenghtOfColumn
    return MaxLength


def get_max_length_on_columns(matrix):
    MaxLengthOnColumns = []
    NumberOfColumns = get_number_of_columns(matrix)
    for column_number in range(NumberOfColumns):
        MaxLengthOnTheColumn = get_max_length_on_column(column_number, matrix)
        MaxLengthOnColumns.append(MaxLengthOnTheColumn)
    return MaxLengthOnColumns

def display_value_of_column(max_length_on_column, value):
    ValueToDisplay = ""
    space = " "
    LengthOfValue = len(str(value))
    NumberOfSpaces = max_length_on_column - LengthOfValue
    for i in range(NumberOfSpaces):
        ValueToDisplay += space
    ValueToDisplay += str(value)
    return ValueToDisplay

def display_row(row, max_length_on_column):
    RowToDisplay = ""
    ColumnNumber = 0
    for Column in row:
        RowToDisplay += display_value_of_column(max_length_on_column[ColumnNumber], Column) + "  "
        ColumnNumber += 1
    return RowToDisplay

def display_matrix(matrix):
    MaxLengthForEachColumns = get_max_length_on_columns(matrix)
    for Row in matrix:
        print(display_row(Row, MaxLengthForEachColumns))

Matrix = create_matrix(3, 3)
display_matrix(Matrix)
