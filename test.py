ingava = ["chocolate", "vanilla"]
toppava = ["sauce", "stawbeery"]

condition = True

print(f"""Welcome to the Cream shop """)

while condition:
    print("Ingredient Available are..")
    for i in ingava:
        print(i)
    user_ingava = input("Enter ingredient from the option above: ").lower()
    print(f"you have selected {user_ingava}")

    print(f"Now Select Topping, Topping available are...")
    for x in toppava:
        print(x)

    user_toppava = input("Enter the topping from the option above: ").lower()

    output = f"you have selected {user_ingava} ingredient with {user_toppava} topping"
    print("Are you Sure....")
    yes_no = input("Enter Yes or No").lower()
    if yes_no == "no":
        continue
    elif yes_no != "yes":
        print(f"wrong input select again: ")
        continue
    else:
        if not (user_ingava or user_toppava):
            print("wrong selection select again")
            continue
        if (user_ingava not in ingava) and (user_toppava not in toppava):
            print("Wrong selection select again")
            continue
        else:
            print(f"your order has been booked and please wait")
            break

print("come again")
