def rotate(array, times):

    if times > len(array):
        times = times % len(array)

    for i in range(len(array) - 1):
        array[i], array[i+1] = array[i+1], array[i]


def left_rotate(array, times):
    for i in range(times):
        first = array[0]
        for i in range(len(array)-1):
            array[i] = array[i+1]

        array[-1] = first


n, d = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

if len(array) == n:
    rotate(array)


for i in array:
    print(i, end=' ')
