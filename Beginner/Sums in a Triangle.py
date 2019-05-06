''' In the first line integer n - the number of test cases (equal to about 1000).
Then n test cases follow. Each test case starts with the number of lines which is followed by their content. '''

n = int(input())
db = []

for i in range(n):
    lines = int(input())
    temp = []
    for j in range(lines):
        if j == 0:
            temp.append([int(input())])
            continue

        temp.append(list(map(int, input().split(' '))))
    db.append(temp)


result = []

for i in db:
    max = 0
    for j in range(len(i) - 1):
        for k in range(len(i[j])):
            if sum([i[j][k], i[j+1][k]]) > max:
                max = sum([i[j][k], i[j+1][k]])
            if sum([i[j][k], i[j+1][k], i[j+1][k+1]]) > max:
                max = sum([i[j][k], i[j+1][k], i[j+1][k+1]])
    result.append(max)


for i in result:
    print(i)





