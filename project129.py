import  csv
import pandas as pd

dataset_1=[]
dataset_2=[]

with open("stars.csv","r") as f:
    csvreader= csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open('unit_converted_stars.csv','r') as e:
    csvreader_2= csv.reader(e)
    for row_2 in csvreader_2:
        dataset_2.append(row_2)

header_1= dataset_1[0]
data_1= dataset_1[1:] 

header_2= dataset_2[0]
data_2= dataset_2[1:]

headers= header_1+header_2
data= []
for i in data_1:
    data.append(i)

for a in data_2:
    data.append(a)

with open('final_stars.csv','w') as f:
    csvwriter= csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)

