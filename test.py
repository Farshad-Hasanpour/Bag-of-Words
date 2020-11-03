from bag_of_words import BagOfWords
# Test
a = BagOfWords(['hello darkness my,. old old friend friend', 'hello how are you my friend'], 3)
print(a.data_entries)
print(a.wordfreq)
print(a.most_frequent)
print(a.corpus_bow())
print(a.text_to_bow('hello'))