t = int(input())
result = []

for i in range(t):
    db = list(map(int, input().split(' ')))

    if sum(db) == 180:
        result.append('YES')
    else:
        result.append('No')

for i in result:
    print(i)