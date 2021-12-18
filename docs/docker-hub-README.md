# Wait4localstack

A Docker image with the
[wait4localstack](https://pypi.org/project/wait4localstack/) Python package installed on it.  This
means that the CLI script is installed in `/usr/local/bin/wait4localstack`.  That script is set as
the entry point of the image.  Anything provided as a command is then passed as arguments
to the script.

For full documentation, see the project home at https://github.com/locp/wait4localstack

To raise issues please go to https://github.com/locp/wait4localstack/issues

## Examples

### Docker Compose

Given a Docker Compose file like the following:

```yaml
---
version: "3"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME-localstack}"
    image: localstack/localstack:0.13.1
    ports:
      - "127.0.0.1:53:53"                # only required for Pro
      - "127.0.0.1:53:53/udp"            # only required for Pro
      - "127.0.0.1:443:443"              # only required for Pro
      - "127.0.0.1:4510-4530:4510-4530"  # only required for Pro
      - "127.0.0.1:4566:4566"
      - "127.0.0.1:4571:4571"
    environment:
      - SERVICES=${SERVICES-iam}
      - DEBUG=1
      - DATA_DIR=${DATA_DIR- }
      - LAMBDA_EXECUTOR=docker-reuse
      - HOST_TMP_FOLDER=${TMPDIR:-/tmp/}
      - DOCKER_HOST=unix:///var/run/docker.sock
    volumes:
      - "${TMPDIR:-/tmp}/localstack:/tmp/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"

  wait4localstack:
    command: -de http://localstack:4566/health
    container_name: wait4localstack
    depends_on:
      - localstack
    image: "locp/wait4localstack:${DOCKER_IMAGE_TAG-latest}"
```

Run the following command to bring up Localstack and wait for it to be ready:

```shell
docker-compose -f examples/docker-compose.yml run --rm wait4localstack
```
