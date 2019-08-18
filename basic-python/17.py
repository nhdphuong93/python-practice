"""
17. Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The
transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100

Then, the output should be:
500
"""

totalAmount = 0

while True:
    inputData = raw_input()

    if not inputData:
        break

    transactionLog = inputData.split(" ")
    if len(transactionLog) != 2:
        break

    transactionType = transactionLog[0]
    amount = int(transactionLog[1])

    if transactionType == "D":
        totalAmount = totalAmount + amount
    elif transactionType == "W":
        totalAmount = totalAmount - amount
    else:
        pass

print totalAmount
