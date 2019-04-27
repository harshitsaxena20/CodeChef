"""
Find occurance of four

Input:

Output:

"""

def four(num):
    count = 0
    while num >0 :
        if num%10 == 4:
            count += 1


        num /= 10
        num = int(num)
    return count

T = int(input())
l = []
for i in range(T):
    l.append(int(input()))

for i in l:
    print(four(i))