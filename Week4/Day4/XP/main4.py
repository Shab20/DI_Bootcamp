import random

def random_number_game(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        print("Success! Both numbers are the same:", num)
    else:
        print("Fail. Number generated:", random_num, "Number entered:", num)