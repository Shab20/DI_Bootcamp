sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich",                   "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("Deli has run out of pastrami")
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

for sandwich in sandwich_orders:
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nFinished Sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)