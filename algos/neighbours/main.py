
import sys

data = []
data = sys.stdin.readlines()

matrix = data[2:-2]

matrix = [list(map(int, row.split())) for row in matrix]

# get neighbors for matrix
def get_neighbors(matrix, row, col):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            # skip diagonals
            if i != 0 and j != 0:
                continue
            if i == 0 and j == 0:
                continue
            if row + i < 0 or row + i >= len(matrix):
                continue
            if col + j < 0 or col + j >= len(matrix[0]):
                continue
            neighbors.append(matrix[row + i][col + j])
    neighbors.sort()
    # return array as string
    return ' '.join(map(str, neighbors))


print(get_neighbors(matrix, int(data[-2]), int(data[-1])))