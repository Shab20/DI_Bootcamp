def create_dictionary(word):
    dictionary = {}
    for i, letter in enumerate(word):
        if letter not in dictionary:
            dictionary[letter] = []
        dictionary[letter].append(i)
    return dictionary

word = "froggy"
result = create_dictionary(word)
print(result)