#list of items
#item prices
#item quantity


items = {

    "Bulad": 15,
    "Sting Red": 25,
    "Sisig": 70,
    "Nuggets":60,
    "Crinkles":6
}

cart = []
flag = 1
#while loop para na naay flag variable
while flag == 1:
    print("Welcome to the Sisigan Store! Here are the items available:")
    for item, price in items.items():
        print(f"{item}: ₱{price}")
    print("Enter the item you want to buy (or type 'done' to finish):")
    input_item = input()
    if input_item == "done":

        #resibo 
        print("----------------Thank you for shopping with us! Here are the items in your cart:----------------")
        for item, quantity in cart:
            print(f"{item}: {quantity} pcs")
        print("Your total is:")
        total = sum(items[item] * quantity for item, quantity in cart)
        print(f"₱{total}")
        print("------------------------------------------Please pay at the counter.------------------------------------------")
        break


    elif input_item in items:
        print(f"How many {input_item} do you want to buy?")
        try:
            quantity = int(input())
            
            if quantity > 0:
                cart.append((input_item, quantity))
                print(f"{quantity} {input_item}(s) added to your cart.")
                print(f"Your cart now contains:")
                print(cart)
            else:
                print("Please enter a valid quantity.")
        except ValueError:
             print("-----------------Please enter an integer to indicate an amount.-----------------")