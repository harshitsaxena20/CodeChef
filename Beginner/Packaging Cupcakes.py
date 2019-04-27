"""

Input: Input begins with an integer T, the number of test cases.
       Each test case consists of a single integer N, the number of cupcakes.

Output: For each test case, output the package size that will maximize the number of
        leftover cupcakes. If multiple package sizes will result in the same number of
        leftover cupcakes, print the largest such size.

"""

"""T = int(input())
cupcakes = []
for i in range(T):
    cupcakes.append(int(input()))

min = 0
for i in cupcakes:
    if i < min:
        min = i"""
n = int(input())
for i in range(1, n+1):
    k = int(input())
    print(int(k/2)+1)
