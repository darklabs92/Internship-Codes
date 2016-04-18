# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 11:20:21 2016

@author: Vidyut Singhania
"""
#########

### This program checks whether the particular input file has completed processing.
### If, it has started - the file name is supposed to have '_processing' appended at the end of the file name
### In case, the output is not present, but the file has been processing for some time, this code is deployed
### This code resets the file state to NOT PROCESSED 

#########

import os

storage='C:/Users/Vidyut Singhania/Downloads/FinalProgram/datasets/trial/rename/'
os.chdir(storage)
onlyfiles = [f for f in listdir(storage) if isfile(join(storage, f))]

outp = 'C:/Users/Vidyut Singhania/Downloads/FinalProgram/datasets/trial/output/'
processed_files = [f for f in listdir(outp) if isfile(join(outp, f))]


inp=[]
for m in onlyfiles:
    #print m
    #print type(m)
    #print m[-16:-5]
    
    if(m[-16:-5]=="_processing"):
        checkName=m[16:-16]
        flg=0        
        for a in processed_files:
            if(checkName==a[0:-4]):
                flg=1
                print checkName, " has completed processing"
        if flg!=1:
            print checkName, "will be restarted for processing"
            os.rename(m, m[:-16]+'.xlsx')
    else:
        checkName=m[16:-5]
        print checkName, "has not been processed"


