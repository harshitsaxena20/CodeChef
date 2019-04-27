"""
The purpose of this problem is to verify whether the method you are using to read
input data is sufficiently fast to handle problems branded with the enormous
Input/Output warning. You are expected to be able to process at least 2.5MB of
input data per second at runtime.

"""

init = input().split()  # init[0] = n & init[1] = k
count = 0
for i in range(int(init[0])):
    num = int(input())
    if num % int(init[1]) == 0:
        count += 1
print(count)
