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
while flag == 1:
    print("Welcome to the Sisigan Store! Here are the items available:")
    for item, price in items.items():
        print(f"{item}: ${price}")
    print("Enter the item you want to buy (or type 'done' to finish):")
    input_item = input()
    if input_item == "done":
        break
    elif input_item in items:
        print(f"How many {input_item} do you want to buy?")
        quantity = int(input())
        if quantity > 0:
            cart.append((input_item, quantity))
            print(f"{quantity} {input_item}(s) added to your cart.")
            print(f"Your cart now contains:")
            print(cart)
        else:
            print("Please enter a valid quantity.")