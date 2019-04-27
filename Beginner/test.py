array = ['1', '2']
for i in range(len(array)):
    array.append(int(array[i]))

for i in range(int(len(array) / 2)):
    del (array[0])

print(array)