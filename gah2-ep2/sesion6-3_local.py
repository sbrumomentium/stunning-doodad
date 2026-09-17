balance = 10000

def withdraw(amount):
    global balance
    balance = balance - amount
    print(balance)
withdraw(2000)
def deposit(amount):
    global balance
    balance = balance + amount
    print(balance)
deposit(500)
