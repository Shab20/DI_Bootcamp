def movie_ticket_price(age):
    if age < 3:
        return 0
    elif age <= 12:
        return 10
    else:
        return 15

def calculate_total_cost(family):
    total_cost = 0
    for person, age in family.items():
        cost = movie_ticket_price(age)
        total_cost += cost
        print(f"{person} has to pay {cost} dollars")
    print(f"The family's total cost is {total_cost} dollars")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
calculate_total_cost(family)

# Bonus
family = {}
while True:
    name = input("Enter a name (or type 'q' to quit): ")
    if name == 'q':
        break
    age = int(input("Enter age: "))
    family[name] = age

calculate_total_cost(family)