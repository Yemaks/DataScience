def transposition(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    transposed_matrix = [[0 for j in range(lines)] for i in range(columns)]
    for i in range(lines):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]
    print("Транспонированная матрица:")
    for i in range(columns):
        for j in range(lines):
            print(transposed_matrix[i][j], end=' ')
        print()
    print("Размер исходной матрицы n, m: " + str(lines) + ", " + str(columns))
    print("Размер транспонированной матрицы n, m: " + str(columns) + ", " + str(lines))


transposition([[1, 2, 4, 29],
               [3, 4, 6, 1]])
