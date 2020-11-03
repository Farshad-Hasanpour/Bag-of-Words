from bag_of_words import BagOfWords
corpus = [
	'most of the statistical algorithms, e.g machine learning and deep learning techniques, work with numeric data',
	'bag of words converts text to numbers'
]
number = 3
bow = BagOfWords(data_entries=corpus, number_of_most_frequent_words=number)

print(bow.data_entries)
print(bow.wordfreq)
print(bow.most_frequent)
print(bow.corpus_bow())
print(bow.text_to_bow('machine learning'))
