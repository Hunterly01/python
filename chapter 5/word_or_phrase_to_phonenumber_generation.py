def words_to_phone_numbers(words):
    keypad =  {
        'A': '1', 'B': '1', 'C': '2', 'D': '2', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    phone_numbers = ""
    words = words.upper()
    for letter in words:
        if letter.isalpha():
            phone_numbers += keypad[letter]
        else:
            phone_numbers += letter
    return phone_numbers

result = "Huntera lee"
print(words_to_phone_numbers(result))


