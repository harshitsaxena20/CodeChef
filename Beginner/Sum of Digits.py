"""
You're given an integer N. Write a program to calculate the sum of all the digits of N.

Input: The first line contains an integer T, total number of testcases.
       Then follow T lines, each line contains an integer N.

Output: Calculate the sum of digits of N.

"""


def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number -= number%10
        number /= 10

    return int(sum_digits)


T = int(input())
l = []
for i in range(T):
    if 1 <= T <= 1000:
        number = int(input())
        if 1 <= number <= 1000000:
            l.append(number)

for i in l:
    print(sum_of_digits(i))




