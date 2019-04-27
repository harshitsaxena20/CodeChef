"""
Program is very simple, Given two integers A and B, write a program to add these two numbers.

Input: The first line contains an integer T, total number of test cases.
       Then follow T lines, each line contains two Integers A and B.

Output: Add A and B and display it.

"""

T = int(input())
output = []
if 1 <= T <= 1000:
    for i in range(T):
        adder_input = input().split()

        if 1 <= int(adder_input[0]) <= 10000 and 1 <= int(adder_input[1]) <= 10000:
            output.append(int(adder_input[0]) + int(adder_input[1]))
    for i in output:
        print(i)

