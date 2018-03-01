import os

os.system("ps -aux | grep plot_ > tmp_clean")

with open ("tmp_clean") as f:
  l = f.readlines()

if len (l) > 10 :
  cpt = 0
  for i in l:
    cpt +=1
    if cpt > 7:
      parse = i.split(" ")
      os.system("kill "+parse[4])
      