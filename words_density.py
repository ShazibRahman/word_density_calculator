
import matplotlib.pyplot as plt
 

import seaborn as sns
sns.set()
den=list()

density=float()
count=int()
count_n=list()

n_words=0
file=open('data.txt','r')
lines1=file.read().split()
data_file=lines1
lines1=" ".join(lines1)
file.close()
print(f"data found in file data.txt in:\n{lines1}\n")


n_words=len(data_file)
print("no of total words",n_words,"\n")
#print(n_words)

file=open('waaa.txt','r')
lines2=file.read().split()
exlusion_file=lines2
lines2=" ".join(lines2)
print(f'words found in exclusion file: {lines2}')
file.close()
    
list_d=[i for i in data_file if i not in exlusion_file]
list_d=set(list_d)#getting over with repeating data 
list_d=list(list_d)
list_d.sort()

print(f'set of words not in exclusion but in data file:\n{list_d}\n')

for i in list_d:
    count=0
  
    count=lines1.count(i)
    print(f'no of word --{i}---  found is {count}')
    count_n.append(count)
    density=round(count/n_words,3)
    print(f'density of ---{i}--- is  {density}')
    
    den.append(density)
Fig=plt.figure(figsize=(15,12))
ax=Fig.add_axes([0.1,0.12,0.4,0.8])
ax1=Fig.add_axes([0.56,0.12,0.4,0.8])
ax1.plot(list_d,count_n,color="#00b3b3",linewidth=3,marker='o',markersize=10,markeredgewidth=3,markerfacecolor="yellow",markeredgecolor="blue")
ax1.axhline(y=0,color="red",linestyle="dashdot",alpha=0.3)
ax1.axvline(x=0,color="red",linestyle="dashdot",alpha=0.3)
ax1.set_title("No_Of_Occurances_Of_Words")
ax1.set_xlabel("\nWords_Name")
ax1.set_ylabel("Occurances")  
ax1.legend(["Plot_graph of Words vs Occurances"]) 

ax.bar(list_d,den,color="blue",width=.4,alpha=.9,edgecolor="yellow")
ax.set_title("Density_Of_Words")
ax.set_xlabel("\nWords_Name")
ax.set_ylabel("Density")  
ax.legend(["Bar_graph of Words vs Density"]) 
#plt.savefig('/media/shazib/Data/py_project/ple.png',figsize=(15,12),dpi=400)
plt.show()