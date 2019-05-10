t = int(input())
db = []
for i in range(t):
    db.append(int(input()))


for n in db:
    if n < 10:
        print('What an obedient servant you are!')
    else:
        print(str(-1))