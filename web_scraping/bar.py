import matplotlib.pyplot as plt
from words import most_occur

font = {'size'   : 7}

plt.rc('font', **font)

fig, ax = plt.subplots()

freq=[]
word=[]
for x in range(len(most_occur)):
	freq.append(most_occur[x][1])
for i in range(len(most_occur)):
	word.append(most_occur[i][0])
ax.bar(word, freq)
plt.xticks(rotation='vertical')
plt.show()