import time
import os

cpt = 0
while True:

  #Every Secondes
  os.system('python3.5 ~/monitor/get/ram1s.py')
  os.system('~/monitor/var/clean_ram.sh &')
  
  if cpt%2==0:
    os.system('python3.5 ~/monitor/script/plot_ram1s.py &')
  
  
  #Every Minutes
  if cpt%60==0:
    os.system('python3.5 ~/monitor/get/net1m.py &')
    os.system('~/monitor/var/clean_net.sh &')
    os.system('python3.5 ~/monitor/script/plot_net30m.py &')
    os.system('cp ~/monitor/graph/* ~/monitor/www')
  
  #Every 4 min
  if cpt%240 == 0:
    os.system('python3.5 ~/monitor/get/net4m.py &')
    os.system('python3.5 ~/monitor/script/plot_net2h.py &')
    
  #Every 10 min
  if cpt%600 == 0:
    os.system('python3.5 ~/monitor/get/disk10m.py &')
    os.system('~/monitor/var/clean_disk.sh &')
    os.system('python3.5 ~/monitor/script/plot_disk10m.py &')
    
  #Every 12 min
  if cpt%720 == 0:
    os.system('python3.5 ~/monitor/get/net12m.py &')
    os.system('python3.5 ~/monitor/script/plot_net6h.py &')
  
  
    
  cpt+=1
  time.sleep(1)

