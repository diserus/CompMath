def matrixRead():
    with open("matrix.txt", 'r') as file:
        matrix = []
        for line in file:
            row = [float(num) for num in line.strip().split()]
            matrix.append(row)
    return matrix
def matrixPrint(matrix):
    for row in matrix:
        for col in row:
            print(int(col),end=" ")
        print()
    print()
def gaussianElimination(matrix):
    n = len(matrix)

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента в столбце (частичный выбор главного элемента)
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        vedusch = matrix[i][i]
        if vedusch == 0:
            raise ValueError("Нет решения")
        for j in range(i, n + 1):
            matrix[i][j] /= vedusch

        # Обнуление всех элементов ниже текущего ведущего
        for k in range(i+1, n):
            factor = matrix[k][i]
            for j in range(0, n + 1):
                matrix[k][j] -= factor * matrix[i][j]
        print(f"Обнулен {i} столбец\n")
        matrixPrint(matrix)

    # Обратный ход
    x = [0]*n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]

    return x
if __name__ == "__main__":
    matrix = matrixRead()
    print("Исходная матрица")
    matrixPrint(matrix)
    solution = gaussianElimination(matrix)
    for i in range(len(solution)):
        print(f"x{i} = {int(solution[i])}")
