sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches made:")
for finished_sandwich in finished_sandwiches:
    print("- " + finished_sandwich)