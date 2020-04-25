#! /bin/bash
isalive=$(curl -s 'http://172.31.45.191:32000/isalive')
if [ "$isalive" = "true" ]
then
	echo "true"
else
	echo  "false"
fi

