test_case = int(input())

for i in range(test_case):
    perm_int = int(input())
    if perm_int == 0:
        break
    flag = -(perm_int)
    data = list(map(int, input().split()))
    for i in range(1, perm_int+1):
        current = data.index(i)+1
        if data[i-1] == current:
            flag += 1
        else:
            print("not ambiguous")
            break
    if not flag:
        print("ambiguous")

