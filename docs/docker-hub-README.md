# Wait4localstack

A Docker image with the
[wait4localstack](https://pypi.org/project/wait4localstack/) Python package installed on it.  This
means that the CLI script is installed in `/usr/local/bin/wait4localstack`.  That script is set as
the entry point of the image.  Anything provided as a command is then passed as arguments
to the script.

For full documentation, see the project home at https://github.com/locp/wait4localstack

To raise issues please go to https://github.com/locp/wait4localstack/issues
