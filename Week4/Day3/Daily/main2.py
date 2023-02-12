items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20",
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}

wallet_str = input("Enter the amount of cash you have on you: ")
wallet_int = int(wallet_str.replace("$", "").replace(",", ""))

affordable_items = []
for item, cost_str in items_purchase.items():
    cost_int = int(cost_str.replace("$", "").replace(",", ""))
    if wallet_int >= cost_int:
        print(f"You can buy {item}")
        affordable_items.append(item)

if len(affordable_items) > 0:
    affordable_items.sort()
    print(f"You can buy {affordable_items}")
else:
    print("You can buy nothing ;_;")