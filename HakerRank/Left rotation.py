#Pending
def rotate(array, times):

    if times >= len(array):
        times = times % len(array)
    print(times)

    for i in range(times):
        for j in range(len(array) - 1):
            array[j], array[j+1] = array[j+1], array[j]

        print(array)
    

def ans():
    line = input().strip().split(" ")
    N = int(line[0])
    d = int(line[1])
    arr = list(map(int, input().strip().split(" ")))
    arr = arr[d:] + arr[0:d]
    for i in range(N):
        print(arr[i], end=' ')



def left_rotate(array, times):
    for i in range(times):
        first = array[0]
        for i in range(len(array)-1):
            array[i] = array[i+1]

        array[-1] = first


"""n, d = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

if len(array) == n:
    rotate(array, d)"""

ans()


