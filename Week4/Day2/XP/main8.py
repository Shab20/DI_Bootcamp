age = int(input("Enter the age of the person: "))

if age < 3:
    print("The ticket is free.")
elif age >= 3 and age <= 12:
    print("The ticket price is $10.")
else:
    print("The ticket price is $15.")

    total_cost = 0
family = []

while True:
    age = int(input("Enter the age of the person: "))
    if age == 0:
        break
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
    family.append((age, cost))

print("Total cost of all the family’s tickets is: $", total_cost)

teens = ['John', 'Jane', 'Jim', 'Jack']
allowed_teens = []
for teen in teens:
    age = int(input(f"Enter the age of the teen {teen}: "))
    if age >= 16 and age <= 21:
        allowed_teens.append(teen)

print("Final list of allowed teens: ", allowed_teens)