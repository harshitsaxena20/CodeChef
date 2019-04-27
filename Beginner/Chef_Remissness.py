test_case = int(input())
for i in range(test_case):
    a, b = map(int, input().split())
    print("{} {}".format(max(a, b), a+b))