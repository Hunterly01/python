def isPalindrome(word):
	return list(word) == list(reversed(word))



def check_for_palindrome(lst):
	return list(filter(isPalindrome, lst))
