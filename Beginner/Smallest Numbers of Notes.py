t = int(input())
result = []

for i in range(t):
    num = int(input())
    if num/100.0 == int(num/100.0):
        result.append(num/100)
    else:
        counter = int(num/100) + int((num%100)/50) + int(num/10) + int(num/1) + int(num/2)

        result.append(counter)
        
        

print(result)
