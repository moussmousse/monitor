import psutil
import time
import os

res = psutil.disk_usage('/')
print (res[3])
prnt=""
prnt+=time.strftime("%A %d %B %Y %H:%M*")
prnt+= res[2]
with open("../var/disk.10m", "a") as f:
    f.write(prnt)