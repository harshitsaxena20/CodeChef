def second_highest(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif b < a < c or c < a < b:
        return a
    else:
        return c


test_case = int(input())
for i in range(test_case):
    a, b, c = map(int, input().split())
    print("{}".format(second_highest(a, b, c)))