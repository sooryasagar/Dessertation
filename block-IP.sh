IP=$3
BL_DIR="/var/ossec/etc/lists/IP-blacklist"

echo "$IP:Attacking IP" >> $BL_DIR
sleep 5
#/var/ossec/bin/wazuh-control restart
