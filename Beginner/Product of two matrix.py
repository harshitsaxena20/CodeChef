A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):

    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

print(result)






