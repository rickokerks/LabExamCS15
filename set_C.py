#accept mobile number
#load amount
#store transactions
#display total per number

transactions = []

def load():
    loop = True
    while loop:
        print("")
        print("[-----BUY LOAD-----]")
        print("")
        number = input("Enter your mobile number: ")
        amount = float(input("Enter the amount: "))
        print("Transaction recorded.")
        transactions.append((number, amount))

        con = input("continue? Y|N: ").strip().lower()
        if con == 'n':
            break

def details():
    print("")
    print("[--------BALANCE DETAILS-------]")
    print("")
    numbertot = input("Enter mobile number: ")
    total = 0

    tranNUm = 0
    for transaction in transactions:
        if transaction[0] == numbertot:
            tranNUm += 1
            print("Transaction " + str(tranNUm) + ": ₱" + str(transaction[1]))
            total += transaction[1]

            print("")

    print("Total load amount: ₱" + str(total))

looping = True

while looping:
    print("")
    print("[-----CHARMELLE LOADMAXX-----]")
    print("")
    print("[1]Buy Load")
    print("[2]Balance Details")
    print("[3]Exit")
    inputChoice = int(input())

    match inputChoice:
        case 1:
            load()
        case 2:
            details()
        case 3:
            break
        case _:
            print("invalid choice!")
