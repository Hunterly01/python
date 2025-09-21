def remove_duplicates(words):
    new_words = [word.lower() for word in words]
    duplicates = set(new_words)
    order = sorted(duplicates)
    new_list = []
    for word in order:
        new_list.append(word.lower())
    print(new_list)

lst = ["hello", "hello", "hello", "hi", "mommy"]
remove_duplicates(lst)

