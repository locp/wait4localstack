FROM python:3-alpine

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
COPY wait4localstack-*.tar.gz /tmp
RUN pip install /tmp/wait4localstack-*.tar.gz
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
