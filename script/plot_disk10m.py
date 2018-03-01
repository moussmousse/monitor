import matplotlib.pyplot as plt
from datetime import datetime


with open ("../var/disk.10m") as f:
  lines = f.readlines()
time = []
value = []
for i in lines:
  parse = i.split('*')
  time.append(parse[0])
  value.append(parse[1])

for i in range(len(time)):
  time[i]= datetime.strptime(time[i],'%A %d %B %Y %H:%M:%S')
for k in range(len(value)):
  value[k]=float(value[k])
    

plt.figure()
plt.title("Disk use")
plt.plot_date(time,value,fmt="r-")
plt.ylabel('Use %')
plt.grid(True)
plt.xticks(rotation=22)  
plt.savefig("../graph/disk.png")