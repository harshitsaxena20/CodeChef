"""

Write a program to find the remainder when two given numbers are divided.

Input: The first line contains an integer T, total number of test cases.
       Then follow T lines, each line contains two Integers A and B.

Output: Find remainder when A is divided by B.


"""

T = int(input())
l = []
for i in range(T):
    num = input().split()
    l.append(int(num[0]) % int(num[1]))

for i in l:
    print(i)