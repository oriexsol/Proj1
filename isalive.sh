#! /bin/bash

node_ip=$1
node_port=$2

erez=$(curl -s 'http://$node_ip:$node_port/isalive')
if [ "$erez" = "true" ]
then
	echo "true"
else
	echo  "false"
fi
