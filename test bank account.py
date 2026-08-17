from bank_account import BankAccount


# 1
account = BankAccount("Ken", 2000)

if account.get_balance() == 2000:
    print("1. pass    account starts with 2000 got", account.get_balance())
else:
    print("1. FAIL    account starts with 2000 got", account.get_balance())


# 2
account = BankAccount("Ken", 2000)
account.deposit(300)

if account.get_balance() == 2300:
    print("2. pass    adding 300 to 2000 gives 2300 got", account.get_balance())
else:
    print("2. FAIL    adding 300 to 2000 gives 2300 got", account.get_balance())


# 3
account = BankAccount("Ken", 2000)
account.withdraw(400)

if account.get_balance() == 1600:
    print("3. pass    taking 400 from 2000 gives 1600 got", account.get_balance())
else:
    print("3. FAIL    taking 400 from 2000 gives 1600 got", account.get_balance())


# 4
account = BankAccount("Ken", 2000)

if str(account) == "Ken: 2000.00":
    print("4. pass    account shows owner and balance got", str(account))
else:
    print("4. FAIL    account shows owner and balance got", str(account))


# 5
account = BankAccount("Ken", 500)

try:
    account.withdraw(600)
    print("5. FAIL    withdrawal above balance is rejected got accepted")
except ValueError:
    print("5. pass    withdrawal above balance is rejected got refused")


# 6
account = BankAccount("Ken", 500)

try:
    account.deposit(-100)
    print("6. FAIL    negative deposit is rejected got accepted")
except ValueError:
    print("6. pass    negative deposit is rejected got refused")


# 7
try:
    account = BankAccount("Ken", -500)
    print("7. FAIL    negative starting balance is rejected got accepted")
except ValueError:
    print("7. pass    negative starting balance is rejected got refused")
