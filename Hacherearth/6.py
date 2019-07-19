case = int(input())

db = []
result = []

for i in range(case):
    a = list(map(int, input().split(' ')))
    db.append(a)

for i in db:
    a, b, c = i[0], i[1], i[2]

    count = 0
    while a != b:

        if a < b:
            a *= c


        elif a > b:
            if a-2 >= b:
                a -= 2
            elif a-2 <= b:
                a -= 1
            else:
                pass

        else:
            break

        count += 1
    result.append(count)


for i in result:
    print(i)





