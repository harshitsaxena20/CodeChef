"""
You are asked to calculate factorials of some small positive integers.

input: An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines,
       each containing a single integer n, 1<=n<=100.

"""


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


times = int(input())
inputs = []

for i in range(times):
    inputs.append(int(input()))

for i in inputs:
    print(factorial(i))



