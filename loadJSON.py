# -*- coding: utf-8 -*-
"""
Created on Thu Mar 03 17:33:15 2016

@author: Vidyut Singhania
"""

import json
import codecs 

with open('C:/Users/Vidyut Singhania/Downloads/twitter/profile/bethguido3.JSON') as data_file:    
   data = json.load(data_file)
    
data = []
with codecs.open('C:/Users/Vidyut Singhania/Downloads/twitter/profile/bethguido3.JSON','rU','utf-8') as f:
    for line in f:
       data.append(json.loads(line))

