#!/bin/bash
echo "$(date): " >> /var/log/cron.log 2>&1
/usr/local/bin/python /usr/src/app/zeabur_extend_trial/main.py >> /var/log/cron.log 2>&1