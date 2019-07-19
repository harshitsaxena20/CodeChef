l = int(input())

num = int(input())

db = []

result = []

for i in range(num):
    a = list(map(int, input().split(' ')))
    db.append(a)

for i in db:
    w, h = i[0], i[1]

    if w<l or h<l:
        result.append('UPLOAD ANOTHER')

    else:

        if w==h:
            result.append('ACCEPTED')
        else:
            result.append('CROP IT')


for i in result:
    print(i)
