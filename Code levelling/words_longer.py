def long_word(word):
	return len(word) > 5
	



def extract_words_thats_longer(words):
	return list(filter(long_word, words))