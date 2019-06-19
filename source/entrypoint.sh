#!/bin/sh

set -e

#Program:
#	echo python file into crontabfile && cron log
# History:
# 2019/06/15	Kent1201	First release

echo 'INFO : In entrypoint.sh'
touch /etc/cron.d/hello-cron
chmod 0644 /etc/cron.d/hello-cron
touch /var/log/cron.log


# Check if our environment variable has been passed.

if [ -z "${CRON}" ]
then
	# curl_script.py with URL
	if [ ! -z "${URL}" ]
	then
		echo 'This is curl_script.py with env URL : ${URL}.'
		/usr/bin/python3.5 /source/${EXE} ${URL}
	# main.py
	elif [ -z "${URL}" ]
	then
		echo 'This is main.py'
		/usr/bin/python3.5 /source/${EXE} 
	else
		echo "ERROR : CRON."
	fi
#check.py
elif [ ! -z "${CRON}" ]
then
	if [ ! -z "{URL}" ]
	then
		echo "* * * * * echo Hell0 w0r1d for yOu" >> /etc/cron.d/hello-cron
		echo "${CRON} /usr/bin/python3.5 /source/${EXE}" >> /etc/cron.d/hello-cron
		crontab /etc/cron.d/hello-cron
		echo "INFO : cron started"
		cron && tail -f /var/log/cron.log
	fi
else
	echo "ERROR : ENV ERROR"
	echo "CHECK : cron : ${CRON}"
        echo "CHECK : url :  ${URL}"
	echo "CHECK : exe : ${EXE}"
fi
