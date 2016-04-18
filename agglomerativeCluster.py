# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:22:57 2015

@author: Vidyut Singhania
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
from nltk.stem.porter import PorterStemmer
from sklearn import feature_extraction
from scipy.cluster import hierarchy
from nltk.stem.porter import *
from collections import Counter
import numpy as np
import pandas as pd
import scipy
from nltk import FreqDist
import nltk
import re
import os
import codecs
import string
import mpld3
import datetime
import math
import openpyxl
import csv

start = datetime.datetime.now().time()


# open the workbook provided
#
wb = openpyxl.load_workbook('C:\\Users\\Vidyut Singhania\\Downloads\\DEF.xlsx')
sheet = wb.get_active_sheet()
stop = nltk.corpus.stopwords.words('english')

# obtain the column named 'content'
p=0
for cell1 in sheet.rows[0]: # get first row
    if (cell1.value=="Content" or cell1.value=="content"):
        break
    else:
        p=p+1
print (p)


# view the name of columns in the sheet
n=0
for i in sheet.rows[0]:
    print(i.value, ' ', type(i.value),'\n',n)
    n+=1


def get_tokens(sheet):
    # store the contents of the comments in a tuple called 'txt'
    txt=()
    for cellObj in sheet.columns[p]:
           txt = txt + (cellObj.value,)
   
    # remove the title 'content'
    txt1 = ()
    for i in range(1,len(txt)): 
        m=" "
        for j in nltk.word_tokenize(txt[i]):
            if j not in stop:
                    j=j.lower()
                    m = ' '.join([m,j])
        txt1 = txt1+ (m,)
    return txt1,txt
    
txt1,txt=get_tokens(sheet)

txt1[1]
type(txt)
fd = FreqDist( w for w in nltk.word_tokenize(txt1))
FreqDist(txt1).plot