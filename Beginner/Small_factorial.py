def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

def fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

test_case = int(input())
for i in range(test_case):
    num = int(input())
    print(fact(num))