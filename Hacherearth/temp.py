inp = [1, 2, 3, 4, 5]
result = []

for i in range(0, len(inp)):
    result.append(1)

for i in range(0, len(inp)):

    for j in range(0, len(result)):

        if i == j:
            continue

        result[i] *= inp[j]


print(result)