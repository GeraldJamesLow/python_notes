
#* Absolute value of (primary diagonal - secondary diagonal) in a 2d square matrix

matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

#? Primary diagonal = 11 + 5 + (-12) = 4
#? Secondary diagonal = 4 + 5 + 10 = 19

def diagonalDifference(arr):
    # Write your code here
    num_row = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0
    for i in range(num_row):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][-i-1]
    return abs(primary_diagonal - secondary_diagonal)

print(diagonalDifference(matrix))