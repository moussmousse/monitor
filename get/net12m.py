import time

    
with open ("../var/net.2h") as f:
  lines = f.readlines()

valup=[]
valdn=[]
name = []
fst = True
for i in lines[-4:]:
  parse1=i.split('*')
  parse2=parse1[1].split("|")
  
  if fst:
    for j in parse2:
      parse3=j.split(';')
      if parse3[0]!='\n':
        name.append(parse3[0])
        valup.append(0)
        valdn.append(0)
    fst = False
  for j in parse2:
    parse3=j.split(";")
    for k in range(len(name)):
      if name[k] == parse3[0]:
        valup[k]+=int(parse3[1])
        valdn[k]+=int(parse3[2])

prnt = ""
prnt+=time.strftime("%A %d %B %Y %H:%M*")
for i in range(len(name)):
  prnt+=(name[i]+";"+str(valup[i]//4)+";"+str(valdn[i]/4)+"|")
prnt+="\n"
with open("../var/net.6h", "a") as f:
    f.write(prnt)