tail -n 300 ~/monitor/var/ram.1s >> tmp_ram
rm ~/monitor/var/ram.1s
mv tmp_ram ~/monitor/var/ram.1s

tail -n 300 ~/monitor/var/ram.1m >> tmp_ram2
rm ~/monitor/var/ram.1m
mv tmp_ram2 ~/monitor/var/ram.1m
