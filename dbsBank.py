# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:15:55 2015

@author: Vidyut Singhania
"""

import io
import os
import pickle

# set the basic path where all the files are stored
#
path = 'F:\\DBS_Test\\HotelReviews'

# determine all the '.dat' files in the given directory location
#
text_files = [f for f in os.listdir(path) if f.endswith('.dat')]

# fileContent will be a matrix containing the content of each review for each hotel
#
fileContent =[]

# fileContent will be a matrix containing the date of each review for each hotel
#
fileDate = []

# fileDate[i][0] and fileContent[i][0] contain the name of the hotel they are storing content about

# create an algorithm which locates each Hotel file, extracts the content and date of each review for the concerned hotel 
# and then stores it in fileContent and fileDate
#
for a in range(len(text_files)):
    dat=[]
    filePath=path+"\\"+text_files[a]
    lines = open(filePath, 'r',encoding="utf8").readlines()
    for line in lines:
            item = line.rstrip()
            # get rid of the extra line seperating each review
            if item=='':
                continue
            else:
                dat.append(line)
                
    txt=[text_files[a]]
    txtDate=[text_files[a]]
    for m in range(len(dat)):
        if(m%2==0):
            p=dat[m]
            txt.append(p[9:len(p)-1])
            print (m,'1',m%2,len(txt),len(txtDate))
            continue
        elif(m%2==1):
            o=dat[m]
            txtDate.append(o[6:len(o)-1])
            print (m,'2',m%2,len(txt),len(txtDate))
    
    # store all the reviews in .txt files corresponding to their hotel name - will apply Stanford Parser on the .txt files
    #
    pat="F:\\DBS_Test\\HotelRev"
    f=open(pat+"\\"+text_files[a][:len(text_files[a])-4]+".txt",'w',encoding='utf-8')
    f.write("\n".join(map(lambda x: str(x), txt[1:])))
    f.close()    
    # add the content of each review for a given hotel in a particular list element of fileContent 
    #    
    fileContent.append(txt)

    # add the date of each review for a given hotel in a particular list element of fileDate 
    #    
    fileDate.append(txtDate)
            
# thus, we now have the entire data files stored in the environment for further processing.
