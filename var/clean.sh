tail -n 100 ~/monitor/var/net.30m >> tmp
rm ~/monitor/var/net.30m
mv tmp ~/monitor/var/net.30m

tail -n 100 ~/monitor/var/net.2h >> tmp
rm ~/monitor/var/net.2h
mv tmp ~/monitor/var/net.2h

tail -n 100 ~/monitor/var/net.6h >> tmp
rm ~/monitor/var/net.6h
mv tmp ~/monitor/var/net.6h

tail -n 100 ~/monitor/var/net.1D >> tmp
rm ~/monitor/var/net.1D
mv tmp ~/monitor/var/net.1D

tail -n 100 ~/monitor/var/net.3D >> tmp
rm ~/monitor/var/net.3D
mv tmp ~/monitor/var/net.3D