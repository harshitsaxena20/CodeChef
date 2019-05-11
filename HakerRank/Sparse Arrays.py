n = int(input())
strings = []
for i in range(n):
    strings.append(input())

q = int(input())
queries = []
#Solved
for i in range(q):
    queries.append(input())

frequecy = {}

for i in strings:
    if i in frequecy.keys():
        frequecy[i] += 1
        continue
    frequecy[i] = 1

result = []

for i in queries:
    if i in frequecy.keys():
        result.append(frequecy[i])
        continue
    result.append(0)

for i in result:
    print(i)