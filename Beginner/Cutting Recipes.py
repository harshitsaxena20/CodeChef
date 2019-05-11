def lcm(db):
    result = None
    for i in db:
        flag = 1
        for j in db:
            if j%i != 0:
                flag = 0
                break
        if (flag and result) == None or (flag and i < result):
            result = i


    return result


    
    
    
t = int(input())
db = []
result = []
for i in range(t):
    db.append(list(map(int, input().split(' '))))

for j in db:
    j = j[1:]
    lc = lcm(j)

    if lc != None:
        result.append(list(int(i/lc) for i in j))
    else:
        result.append(j)


for line in result:
    for elm in line:
        print(elm, end=' ')
         
    print()