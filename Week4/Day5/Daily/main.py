def sort_words(words):
    words_list = words.split(',')
    sorted_words = [word.strip() for word in sorted(words_list)]
    print(', '.join(sorted_words))
    
    sort_words("cat, book, morning, evening")