def ispalindrome(word):
    return word.lower() == word[::-1].lower()

print(ispalindrome('Radar'))
print(ispalindrome('hun'))