FROM python:3-alpine

COPY wait4localstack-*.tar.gz /tmp
RUN ls -l /tmp \
    && pip install /tmp/wait4localstack-*.tar.gz
CMD ["sleep", "infinity"]
