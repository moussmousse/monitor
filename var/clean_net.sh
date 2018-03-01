tail -n 100 ~/monitor/var/net.30m >> tmp
rm ~/monitor/var/net.30m
mv tmp ~/monitor/var/net.30m

tail -n 100 ~/monitor/var/net.2h >> tmp
rm ~/monitor/var/net.2h
mv tmp ~/monitor/var/net.2h

tail -n 100 ~/monitor/var/net.6h >> tmp
rm ~/monitor/var/net.6h
mv tmp ~/monitor/var/net.6h

