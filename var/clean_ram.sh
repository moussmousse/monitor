tail -n 300 ~/monitor/var/ram.1s >> tmp_ram
rm ~/monitor/var/ram.1s
mv tmp_ram ~/monitor/var/ram.1s

