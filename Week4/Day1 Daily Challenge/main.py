import random

user_string = input("Enter a string (10 characters long): ")
if len(user_string) < 10:
    print("string not long enough")
elif len(user_string) > 10:
    print("string too long")
else:
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])
    for i in range(len(user_string)):
        print(user_string[:i+1])

# Bonus
char_list = list(user_string)
random.shuffle(char_list)
jumbled_string = ''.join(char_list)
print("Jumbled string:", jumbled_string)