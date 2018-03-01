import psutil
import time
import os

res = psutil.virtual_memory()

prnt=""
prnt+=time.strftime("%A %d %B %Y %H:%M:%S*")
prnt+= str(res[2])
prnt+= '\n'
with open("../var/ram.1s", "a") as f:
    f.write(prnt)