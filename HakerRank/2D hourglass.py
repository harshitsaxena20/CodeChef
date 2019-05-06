l = [[0, -4, -6, 0, -7, -6], [-1, -2, -6, -8, -3, -1], [-8, -4, -2, -8, -8, -6], [-3, -1, -2, -5, -7, -4], [-3, -5, -3, -6, -6, -6],
     [-3, -6, 0, -8, -6, -7]]

hourglass = []

for i in range(4):

    for j in range(4):

        new = []

        for k in range(3):
            new.append(l[i][j+k])

        new.append(l[i + 1][j + 1])
        for m in range(3):
            new.append(l[i + 2][j+m])

        hourglass.append(new)


sum_max = -2147483647

for i in hourglass:
    if sum(i) > sum_max:
        sum_max = sum(i)
    if(sum(i) == 0):
        print(i)

print(sum_max)
