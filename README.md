# Bag of Words

This code is an implementation for Bag of Words using python.
It helps you to understand the concept of Bag of Words. Check out (Sci-kit Learn)[https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html] for a better and more detailed function to do this.

## Usage

```python
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
```

## Article
This code is implemented with the help of an article written by Usman Malik from [Stack Abuse](https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/)