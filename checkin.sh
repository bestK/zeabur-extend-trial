#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export $(cat /proc/1/environ |tr '\0' '\n' | xargs)

/usr/local/bin/python /app/zeabur_extend_trial/main.py >> /app/cron.log 2>&1