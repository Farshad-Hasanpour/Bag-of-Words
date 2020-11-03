import nltk
from heapq import nlargest
from re import sub


class BagOfWords:
	def __init__(self, data_entries, number_of_most_frequent_words):
		"""
		preprocess of corpus. generation of word frequency and most frequent words
		:param data_entries: list of strings: corpus as a list of strings
		:param number_of_most_frequent_words: int:  pass -1 to get all words
		"""

		# For each sentence in corpus
		for i in range(len(data_entries)):
			data_entries[i] = BagOfWords.__preprocess(data_entries[i])

		# Create word frequency dictionary
		wordfreq = {}
		for sentence in data_entries:
			words = nltk.word_tokenize(sentence)
			for word in words:
				if word not in wordfreq.keys():
					wordfreq[word] = 1
				else:
					wordfreq[word] += 1

		# Use only most frequent words
		if number_of_most_frequent_words < 1:
			most_frequent = list(wordfreq.keys())
		else:
			most_frequent = nlargest(number_of_most_frequent_words, wordfreq, key=wordfreq.get)

		self.data_entries = data_entries
		self.wordfreq = wordfreq
		self.most_frequent = most_frequent

	def corpus_bow(self):
		"""
		:return: list of list of int: bow vector of each corpus entry (data entry)
		"""
		data_entries_bow = []
		for data_entry in self.data_entries:
			entry_words = nltk.word_tokenize(data_entry)
			entry_vector = []
			for feature in self.most_frequent:
				if feature in entry_words:
					entry_vector.append(1)
				else:
					entry_vector.append(0)
			data_entries_bow.append(entry_vector)
		return data_entries_bow

	def text_to_bow(self, text):
		"""
		:param text: list of strings: new text input
		:return: list of int: bag of words for new text input
		"""
		text = BagOfWords.__preprocess(text)
		words = nltk.word_tokenize(text)
		text_vector = []
		for feature in self.most_frequent:
			if feature in words:
				text_vector.append(1)
			else:
				text_vector.append(0)
		return text_vector

	@staticmethod
	def __preprocess(text):
		text = text.lower()  # Data entry to lower case
		text = sub(r'\W', ' ', text)  # Remove punctuation
		text = sub(r'\s+', ' ', text)  # Remove additional spaces
		return text
