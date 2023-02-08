def items_affordable(items_purchase, wallet):
    items_affordable = []
    wallet_value = int(wallet[1:].replace(',', ''))
    for item, price in items_purchase.items():
        item_price = int(price[1:].replace(',', ''))
        if wallet_value >= item_price:
            items_affordable.append(item)
    items_affordable.sort()
    return items_affordable if items_affordable else "Nothing"

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1"