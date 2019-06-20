#!/bin/bash

path="/Path/you/want" 
filename="${path}""/Dockershare/list.txt"
image_name="104321024/imsdb-crawler"


exec < ${filename}

while IFS=' ' read -r url visited 
do
    #echo "${url}"
    #echo "${visited}"
    if [ "${visited}" == "1" ]
    then
	echo "${url} is visited."
    elif [ "${visited}" == "0" ]
    then
    	docker run --rm -dit -v "${path}"/Dockershare:/Dockershare -e EXE="crul_script.py" -e URL="${url}" ${image_name}
        OldLine="${url}"" ""${visited}"
	#echo "OldLine = ${OldLine}"
	visited="1"
	NewLine="${url}"" ""${visited}"
        #echo "NewLine = ${NewLine}"
	sed -e "s|${OldLine}|${NewLine}|g" -i ${filename}
    else
	exit 1
    fi
done
exit 0
