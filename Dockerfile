FROM python:3.9

WORKDIR /usr/src/app

# 安装依赖
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Install Pip
RUN apt update
RUN apt install -y cron

# 设置定时脚本权限
RUN chmod +x checkin.sh

# Add crontab file in the cron directory
ADD cronfile /etc/cron.d/submit-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/submit-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
# 更改时区
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log