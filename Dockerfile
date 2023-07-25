FROM python:3.10

RUN apt-get update && apt-get -y install cron vim
WORKDIR /app

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
COPY . .

RUN chmod +x checkin.sh
RUN pip install --no-cache-dir -r requirements.txt

RUN /usr/bin/crontab /etc/cron.d/crontab && touch /app/cron.log

ENV ZEABUR_API_TOKEN=${ZEABUR_API_TOKEN}

CMD cron -f & tail -f /app/cron.log