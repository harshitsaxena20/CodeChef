"""

If Give an integer N . Write a program to obtain the sum of the first and last digit of this number.

Input: The first line contains an integer T, total number of test cases. Then follow T lines,
       each line contains an integer N.

Output: Display the sum of first and last digit of N.

"""

test_case = int(input())
for i in range(test_case):
    num = int(input())
    print(int(str(num)[0]) + int(str(num)[-1]))

