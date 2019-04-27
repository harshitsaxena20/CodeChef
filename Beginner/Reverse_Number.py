"""
If an Integer N, write a program to reverse the given number.
"""


def inverse(num):
    result = 0
    while num > 0:
        rem = num % 10
        result = (result * 10) + rem
        num = num//10
    return result


test_case = int(input())
for i in range(test_case):
    num = int(input())
    print(inverse(num))