#!/bin/bash

path="/home/kent1201/"
filename="${path}""Dockershare/list.txt" 
image="imsdb-crawler"
count=10
i=0

exec < ${filename}

while IFS=' ' read -r url visited 
do
    echo "${url}"
    #echo "${visited}"
    if [ "${visited}" == "1" ]
    then
	echo "${url} is visited."
    elif [ "${visited}" == "0" ]
    then
    	if [ "$i" -lt "$count" ]
	then
		echo "Creating..."
        	docker run --rm -dit -v "${path}"Dockershare:/Dockershare -e EXE="crul_script.py" -e URL="${url}"  ${image}
        	OldLine="${url}"" ""${visited}"
		#echo "OldLine = ${OldLine}"
		visited="1"
		NewLine="${url}"" ""${visited}"
        	#echo "NewLine = ${NewLine}"
		sed -e "s|${OldLine}|${NewLine}|g" -i ${filename}
		i=$(expr $i + 1)
	elif [ "$i" -eq "$count" ]
	then
		echo "I am sleeping."
		sleep 1m
		i=0
	fi
    else
	exit 1
    fi
done
exit 0
