fruits = "apple mango cherry"
fruits_list = fruits.split(" ")

while True:
    user_input = input("Enter a fruit name: ")
    if user_input in fruits_list:
        print("You chose one of your favorite fruits! Enjoy!")
        break
    else:
        print("You chose a new fruit. I hope you enjoy.")