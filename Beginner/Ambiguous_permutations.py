
result = []
while 1:
    n = int(input())

    if n == 0:
        break

    db = list(map(int, input().split()))
    inv = list(db)

    for i in range(len(db)):
        index = i+1
        element = db[i]
        inv[element-1] = index

    if db == inv:
        result.append('ambiguous')
    else:
        result.append('not ambiguous')


for i in result:
    print(i)




