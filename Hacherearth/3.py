'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


def alter(num):
    if num == 0:
        return 1
    return 0


# Write your code here
size = int(input())
db = [int(input()) for i in range(size)]

for i in range(1, size+1):

    pos = i

    while pos<=size:

        db[pos-1] = alter(db[pos-1])

        pos += i

    print(db)

result = 0

for i in db:
    if i == 1:
        result += 1

print(result)




