# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:30:09 2015

@author: Vidyut Singhania
"""

#######

### This program contains random steps / fns. I practiced in order to ensure I know the function's processing

#######
import openpyxl
from __future__ import print_function
from __future__ import division, unicode_literals
from nltk import FreqDist
import re
import xlrd
import nltk
from bs4 import BeautifulSoup
import datetime
import math
from textblob import TextBlob as tb
import textmining

def is_ascii(s):
    try:
        return all(ord(c) < 128 for c in s)
    except TypeError:
        return False

# open the workbook provided
#
#xl_workbook = xlrd.open_workbook("C:\\Users\\Vidyut Singhania\\Downloads\\abc.xlsx")
wb = openpyxl.load_workbook('C:\\Users\\Vidyut Singhania\\Downloads\\abc.xlsx')
sheet1 = wb.get_sheet_by_name('ABC - SG')
sheet = wb.get_active_sheet()
stop = nltk.corpus.stopwords.words('english')

# store the contents of the comments in a tuple called 'txt'
txt=()
type(txt)

for cellObj in sheet.columns[24]:
       txt = txt + (cellObj.value,)

txt1 = ()
type(txt1)

for i in range(len(txt)): 
    m=" "
    for j in nltk.word_tokenize(txt[i]):
        if j not in stop:
            #if  j.isalpha() :
                m = ' '.join([m,j])
            #else:
             #   m = ''.join([m,j])                
            #print ("\n J : \n",j)
            #print ("\n M : \n",m)
    txt1 = txt1+ (m,)



#for cellObj in sheet.columns[24]:
#    txt1 = txt1 + (cellObj.value,)
 
# store the title of each comment in tuple called 'title'   
title=()
for cellObj in sheet.columns[11]:
       title = title + (cellObj.value,)

# List sheet names, and pull a sheet by name
#
# sheet_names = xl_workbook.sheet_names()
# print('Sheet Names', sheet_names)

# pull the first sheet in the workbook
#
# xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

# slice & dice! :p
# pull only the content part of the excel - the part we are interested in 
#
# txt = xl_sheet.col_slice(24,1)
        


# Tabulate the Frequency Distr. of ftxt in order to determine the stop words we need to remove
full=" "
for i in range(3,len(txt1)):
    full = full+txt[i]


#### construct the tf and tfidf matrices for the given comments.

# returns the term freq of 'word' in 'blob'
def tf(word, blob):
    blob = tb(blob)
    return blob.words.count(word)/float (len(blob.words))
    
# returns the no of docs containing 'word'
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in tb(blob))
    
# computes and returns the inverse doc. freq.
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

# computes and returns the tf-idf score
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
    
x = ( math.log(len(txt) / (1 +   n_containing('the',txt))))

start = datetime.datetime.now().time()
td_matrix = {}
tfidf_matrix = {}
#title[3]
len(txt1)
len(title)


for idx in range(1,len(txt1)):
    post = txt1[idx]
    #fdist = nltk.FreqDist( w for w in nltk.word_tokenize(post))
    doc_title = title[idx]
    link = idx
    #td_matrix[(doc_title, link)] = {}
    tfidf_matrix[(doc_title,link)] = {}
    for term in set(nltk.word_tokenize(post)):
        #td_matrix[(doc_title, link)][term] = tf(term,post)
        tfidf_matrix[(doc_title,link)][term] = tf1(term,post)*idf1(term,txt)
        
end = datetime.datetime.now().time()




vocabulary = []
docs = {}
all_tips = []




def freq1(word, doc):
    return doc.count(word)


def word_count1(doc):
    return len(doc)


def tf1(word, doc):
    return (freq1(word, doc) / float(word_count1(doc)))


def num_docs_containing(word, list_of_docs):
    count = 0
    for document in list_of_docs:
        if freq1(word, document) > 0:
            count += 1
    return 1 + count


def idf1(word, list_of_docs):
    return math.log(len(list_of_docs) /
            float(num_docs_containing(word, list_of_docs)))
            



for idx in range(1,len(txt1)):
    post = txt1[idx]
    #fdist = nltk.FreqDist( w for w in nltk.word_tokenize(post))
    doc_title = title[idx][:50]
    words = set(nltk.word_tokenize(post)
    docs[idx][words] = {'freq': {}, 'tf': {}, 'idf': {}}
    for term in words:
        docs[idx]['freq'][term] = freq1(term, txt1)
        docs[idx]['tf'][term] = tf1(term, txt1)
        

for doc in docs:
    for token in docs[doc]['tf']:
        #The Inverse-Document-Frequency
        docs[doc]['idf'][token] = idf1(token, txt1)
        

end = datetime.datetime.now().time()



            


def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('man'):
        return word[:-3] + 'men'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'
        
def single(text):
    if text.endswith('s'):
        return word[:-1]
        
