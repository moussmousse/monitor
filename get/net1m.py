import psutil
import time
import os

res = psutil.net_io_counters(pernic=True)
up1=[]
dn1=[]
for i in res:
  up1.append(res[i][0])
  dn1.append(res[i][1])
time.sleep(55)
res = psutil.net_io_counters(pernic=True)
prnt=""
prnt+=time.strftime("%A %d %B %Y %H:%M*")
k=0
for i in res:
  prnt+=(i+";"+str((res[i][0]-up1[k])//55)+";"+ str((res[i][1]-dn1[k])//55)+"|")
  k+=1
prnt+="\n"


with open("../var/net.30m", "a") as f:
    f.write(prnt)
print(prnt)