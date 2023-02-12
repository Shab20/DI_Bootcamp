user_input = input("Enter a word please: ")  
char_index_dict = {}

for letter_position, letter in enumerate(
    user_input
):  
    print(f"At position {letter_position}, we have the letter {letter}")
    if (
        letter in char_index_dict.keys()
    ):  
        char_index_dict[letter].append(
            letter_position
        )  
    else:  
        char_index_dict[letter] = [
            letter_position
        ]  

print(char_index_dict)

word_len = 0
for key, position_list in char_index_dict.items():
    for position in position_list:
        if position > word_len:
            word_len = position
word_len += 1
print(f"The word has length {word_len}")

rebuild_index = 0
rebuilt_word = ""
for rebuild_index in range(0, word_len):
    found_letter = False
    for key, position_list in char_index_dict.items():
        for position in position_list:
            if position == rebuild_index:
                rebuilt_word += key
                rebuild_index += 1
                found_letter = True
                break
        if found_letter:
            break

print(f"The rebuilt word is : {rebuilt_word}")