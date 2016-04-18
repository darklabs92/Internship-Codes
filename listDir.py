# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:43:05 2016

@author: Vidyut Singhania
"""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('/co/VD/data') if isfile(join('/co/VD/data', f))]

for nomenclature in onlyfiles:
    print nomenclature
    nomenclature=onlyfiles[0][16:len(onlyfiles[0])-5]
    print type(nomenclature[16:len(nomenclature)-5])
    print