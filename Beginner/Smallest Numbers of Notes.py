t = int(input())
result = []

for i in range(t):
    num = int(input())
    if num/100.0 == int(num/100.0):
        result.append(num/100)
    else:
        counter = 0
        

print(result)
