price = []
basket = []


print("  ***** Welcome to iShop Calculator *****\n")
items_number = int(input("How many items are there in your basket today?:  "))
print("\nLet's get to counting them ....\n")

if items_number > 0:
    for number in range(1, items_number + 1):
        item = input(f"Please tell me the name of the item number {number}:  ").capitalize()
        basket.append(item)
        item_price = float(input(f"What is the price of {item}: \n$"))
        price.append(item_price)

    response = input("Would you like to see your basket items? (Yes/No):  ").capitalize()
    if response == "No":
        input("Press Enter ....")
    else:
        print(basket)

    response = input("Would you like to see how mutch it'll cost? (Yes/No):  ").capitalize()
    if response == "No":
        input("Press Enter to exist ....")
    else:
        print(f"\nBuying these items will cost:  \n${sum(price):.3f}")

else:
    print("Seems like you're not in the mood for shopping today...")
