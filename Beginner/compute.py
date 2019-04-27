cupcakes=int(input("Enter the number of cupcakes "))
a=1
for i in range (cupcakes):
    n=cupcakes%i
    while n!=0:
        for j in range (n):
            if n>a:
                a=n