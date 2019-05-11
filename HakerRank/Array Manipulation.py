#Pending
def arrayManipulation(n, queries):
    #queries: [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    #n: integer
    db = [0 for i in range(n)]

    for i in queries:
        ll, ul, value = i[0]-1, i[1]-1, i[2]

        for j in range(ll, ul+1):
            db[j] += value

    return(max(db))




nm = input().split()

n = int(nm[0])
m = int(nm[1])
queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
