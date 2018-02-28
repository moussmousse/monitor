with open("../var/net.30m") as f:
    l = f.readlines()
put = l[len(l)-1]

with open("../var/net.2h ..", "a") as f:
    f.write(put)