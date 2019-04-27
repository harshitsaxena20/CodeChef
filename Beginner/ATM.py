"""
Pooja would like to withdraw X $US from an ATM. The cash machine will only
accept the transaction if X is a multiple of 5, and Pooja's account balance has
enough cash to perform the withdrawal transaction (including bank charges).
For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's
account balance after an attempted transaction.

"""

pooja = input().split()
withdrawal_amount = int(pooja[0])
balance = float(pooja[1])
charges = 0.50

if withdrawal_amount%5 == 0 and (-withdrawal_amount + balance) >= 0.5:
    balance = balance - withdrawal_amount - charges
    print(balance)
else:
    print(balance)

