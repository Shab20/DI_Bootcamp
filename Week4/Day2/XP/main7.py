toppings = []

while True:
    topping = input("Enter a topping for your pizza, or type 'quit' to stop: ")
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"{topping} will be added to your pizza.")

if toppings:
    print(f"Your pizza with the toppings: {', '.join(toppings)} will cost $10 + $2.5 for each topping, for a total of $" + str(10 + 2.5*len(toppings)))
else:
    print("You didn't order any toppings for your pizza.")