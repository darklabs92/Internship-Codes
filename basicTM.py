# this program runs some generic text analytic commands on the text file, once
# it is placed in the C>Users>(name)>AppData>Roaming>nltk_data>corpora>gutenberg
from __future__ import division
from nltk import FreqDist
#import nltk
from nltk.corpus import gutenberg
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
#import matplotlib

# used to  create our own corpus of random text
corpus_root = 'C:\\Users\\Vidyut Singhania\\AppData\\Roaming\\nltk_data\\corpora\\gutenberg'

# this command enables us to initialize the list of fileids to * (all) files present
wordlists = PlaintextCorpusReader(corpus_root, '.*')

# used to access the words in the fileid 'textmso.txt'
wordlists.words('textm.txt')
fr = FreqDist(wordlists.words('textm.txt'))
print(fr)
f = fr.keys()
fr.plot(50,cumulative=True)
m = sorted(set(fr))
print(m)
wor = [w for w in f if w.isalpha()]
print(wor)
len(wor)
len(f)
w1 = FreqDist(wor)
w1.plot(50,cumulative=False)

# extract only the words from the provided text corpus
k = [k for k in wordlists.words('textm.txt') if k.isalpha()]
# determine the FreqDist for the list of words in the corpus
fr1 = FreqDist(k)
# print the distr.
print(fr1)
# determine the unique elements
w1 = fr1.keys()
print(w1)
len(w1)
fr1.plot(50)
i = ['the']
m = [i for i in fr1 if i in ]
print(m)
m

# We can replace gutenberg with wordlists now. 
# Thus, the txt file need not necessarily have to be placed in the  gutenberg folder anymore. :D

num_chars = len(gutenberg.raw('textm.txt'))               # used to determine the total characters present in text, including blank spaces
num_words = len(gutenberg.words('textm.txt'))             # used to determine the total words present in text
num_distWord = len(set(gutenberg.words('textm.txt')))     # used to determine the total distinct words present in text
num_sents = len(gutenberg.sents('textm.txt'))             # used to determine the total sentences present in text
avg_word_length = num_chars / num_words                     # used to determine the average length of a word in the text
avg_wordsInSent = num_words / num_sents                     # used to determine the average number of words in a sentence in the text
avg_vocab_usage = num_words / num_distWord                  # used to determine the average numer of times words / vocabulary tend to be repeated in the text

print(num_chars,':', "Total number of characters in the text")
print(num_words,':', "Total number of words in the text")
print(num_distWord,':', "Total number of distinct words in the text")
print(num_sents,':', "Total number of words in the text")
print(avg_word_length,':', "Average number of character in each words in the text")
print(avg_wordsInSent,':', "Average number of words in a sentence in the text")
print(avg_vocab_usage,':', "Average times a given word / vocabulary is repeated in the text")

print(gutenberg.words('textmso.txt'))


fr = FreqDist([w for w in gutenberg.words('textm.txt')])
fr.plot(40,cumulative=False)

fr = FreqDist(wordlists.words('textm.txt'))
longest_len = max([len(s) for s in ])
mx = max(len(s) for s in wordlists.words('textm.txt') ) 
fr