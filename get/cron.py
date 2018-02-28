import time
import os

while True:

  os.system('python3.5 net1m.py &')
  print (time.strftime("%H:%M:%S"))
  time.sleep(60)

