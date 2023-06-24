import pandas as pd
import csv
import matplotlib.pyplot as plt

with open('sum.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    row = list(csv_reader)

content={}
no={}
ano={}
j_=0
for x in range(len(row[0])):
	if j_>17:
		ano[row[0][x]]=(row[1][x])
	content[row[0][x]]=(row[2][x])
	j_+=1
content.pop('')
ano_copy=ano.copy()
for x in ano:
	ano_copy[x]=float(ano[x])/50000*10

j=0
content_copy=content.copy()
for x in content_copy:
	if j>9:
		if j<17:
			no[x]=float(content[x])
		content.pop(x)
	j+=1
no_copy=no.copy()
for x in no:
	no_copy[x]=float(no[x])/50000*100

content.update(no_copy)
content.update(ano_copy)
for x in content:
	content[x]=float(content[x])
	content[x]=round(content[x],2)

sorted_con = {}
val=sorted(content.values())
for i in val:
    for k in content.keys():
        if content[k] == i:
            sorted_con[k] = content[k]
            break
sorted_con.pop('booking_origin_Antarctica')
me=[]
ke=[]
font = {'size'   : 7}

plt.rc('font', **font)
for x in sorted_con:
	me.append(float(sorted_con[x]))
for x in sorted_con:
	ke.append(x)
plt.barh(ke, me)
plt.show()