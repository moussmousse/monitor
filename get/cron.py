import time
import os

cpt = 0
while True:

  #Every Secondes
  os.system('python3.5 ~/monitor/get/ram1s.py')
  os.system('~/monitor/var/clean_ram.sh &')
  
  #Every 5 secondes
  if cpt%5==0:
    os.system('python3.5 ~/monitor/script/clean_process.py')
  
  #Every 10 secondes
  if cpt%10==0:
    os.system('python3.5 ~/monitor/script/plot_ram1s.py &')
  
  #Every 30 secondes
  if cpt%30==0:
    os.system('python3.5 ~/monitor/get/ram1m.py')
    os.system('python3.5 ~/monitor/script/plot_ram1m.py &')
  
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
  #if cpt%600 == 0:
  
    #os.system('python3.5 ~/monitor/get/disk10m.py &')
   # os.system('~/monitor/var/clean_disk.sh &')
  #  os.system('python3.5 ~/monitor/script/plot_disk10m.py &')
  
    
  #Every 12 min
  if cpt%720 == 0:
    os.system('python3.5 ~/monitor/get/net12m.py &')
    os.system('python3.5 ~/monitor/script/plot_net6h.py &')
  
  
    
  cpt+=1
  time.sleep(1)

