FROM nginx

ADD ./entrypoint.sh /tmp/entrypoint.sh
ADD ./script.sh /tmp/script.sh

RUN chmod +x /tmp/entrypoint.sh /tmp/script.sh

ENTRYPOINT ["bash","/tmp/entrypoint.sh"]
