import matplotlib.pyplot as plt
from datetime import datetime


with open ("../var/net.30m") as f:
  lines = f.readlines()
time=[]
valup=[]
valdn=[]
name = []
fst = True
for i in lines:
  parse1=i.split('*')
  time.append(parse1[0])
  parse2=parse1[1].split("|")
  
  if fst:
    for j in parse2:
      parse3=j.split(';')
      if parse3[0]!='\n':
        name.append(parse3[0])
        valup.append([])
        valdn.append([])
    fst = False
  for j in parse2:
    parse3=j.split(";")
    for k in range(len(name)):
      if name[k] == parse3[0]:
        valup[k].append(parse3[1])
        valdn[k].append(parse3[2])
  

for k in range (len(valdn)):
  for i in range (len(valdn[k])):
    valdn[k][i]=int(valdn[k][i])//1000
for k in range (len(valup)):
  for i in range (len(valup[k])):
    valup[k][i]=int(valup[k][i])//1000
for i in range (len(time)):
  time[i]= datetime.strptime(time[i],'%A %d %B %Y %H:%M')
  


plt.plot_date(time, valdn[0],label=name[0]+": up",fmt="r-")
plt.plot_date(time,valup[0],label=name[0]+": down",fmt="b-")
plt.ylabel('Debit (Ko\s)')
plt.grid(True)
plt.xticks(rotation=22)
plt.legend()   
plt.savefig('test.png')
