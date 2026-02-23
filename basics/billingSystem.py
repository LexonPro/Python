#Billing system for supermarket

while True:
    name = input("Enter customer's name : ")
    total = 0
    while True:
        print("Now enter amount and quantity")
        amount = float(input("Enter amount : "))
        quantity = float(input("Enter Quantity : "))
        total += amount * quantity
        repeat = input("add more items (Y/N)")
        if(repeat == 'N' or repeat == 'n'):
            break

    print("_"*40)
    print()
    print("Customer's Name : ",name)
    print("Total amaout : ",total)
    print("_"*40)
    print("********* Happy Shopping *************")

    repeat1 = input("Do u want to bill next customer (Y/N)")
    if(repeat1 == 'N' or repeat1 == 'n'):
        break

