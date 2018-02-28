import time
import os

cpt = 0
while True:

  #Every Minutes
  os.system('python3.5 ~/monitor/get/net1m.py &')
  print (time.strftime("%H:%M:%S  -> ") + str(cpt))
  os.system('~/monitor/var/clean.sh &')
  os.system('python3.5 ~/monitor/script/plot_net30m.py &')
  
  #Every 4 min
  if cpt%4 == 0:
    os.system('python3.5 ~/monitor/get/net4m.py &')
    os.system('python3.5 ~/monitor/script/plot_net2h.py &')
  #Every 12 min
  if cpt%12 == 0:
    os.system('python3.5 ~/monitor/get/net12m.py &')
    os.system('python3.5 ~/monitor/script/plot_net6h.py &')
  #Every 48 min
  if cpt%48 == 0:
    a=0
  #Every 2h24min
  if cpt%144 == 0:
    a=0
    
  cpt+=1
  time.sleep(60)

