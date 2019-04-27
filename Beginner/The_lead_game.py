def int_list(array):
    for i in range(len(array)):
        array.append(int(array[i]))

    for i in range(int(len(array)/2)):
        del(array[0])
    return array


result = [0, 0]


for i in range(int(input())):
    a, b = list(map(int, input().split()))

    lead = a - b

    if abs(lead) > result[1]:
        result[1] = abs(lead)
        if lead == abs(lead):
            result[0] = 1
        else:
            result[0] = 2


for i in result:
    print(i, end=' ')
