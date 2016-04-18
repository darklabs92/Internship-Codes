import pandas as pd
import openpyxl
from pandas import ExcelWriter
import csv

book = openpyxl.load_workbook('C:/Users/data56/Downloads/Vidyut/datasets/YObama.xlsx')
sheet  = book.get_active_sheet()

fd=[]
rg=[]
rw=len(sheet.rows)

for i in range(rw):
    rg.append(i)

df = pd.DataFrame({'rng':rg})

for m in range(len(sheet.columns)):
    fd=[]
    ct=0
    print "m=", m
    for cellObj in sheet.columns[m]:
        fd.append(cellObj.value)
        print cellObj.value
        print ct
        ct+=1
    st='col'+str(m)
    df[st]=fd


rev=[]
for uy in reversed(range(rw)):
    rev.append(uy)

df['col10000']=rev

#print df

print 'rw=',rw

# Create a Pandas Excel writer using OpenPyXL as the engine.
writer = pd.ExcelWriter('C:/Users/data56/Downloads/Vidyut/datasets/output1.xlsx', engine='openpyxl')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
print 'rw=',rw