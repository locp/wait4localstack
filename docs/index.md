<!-- wait4localstack documentation master file, created by
sphinx-quickstart on Mon Oct 11 18:31:56 2021.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to wait4localstack’s documentation!

# Wait4Localstack

Wait for Localstack to be ready.

Localstack publishes which services it has been configured to execute and
their status (e.g. “running”).  This module provides a class that will
check that the status of all services are “running”.

### Notes

The service health checks for Localstack are described in detail in the
Localstack documentation see
[https://github.com/localstack/localstack#service-health-checks](https://github.com/localstack/localstack#service-health-checks)

### Examples

To run with defaults simply have:

```python
>>> from wait4localstack import Wait4Localstack
>>> wait4localstack = Wait4Localstack()
>>> wait4localstack.wait_for_all_services()
```


### class wait4localstack.Wait4Localstack(localstack_endpoint='http://localhost:4566/health', maximum_retries=0, test_interval=2, exponential_backoff=False, log_level='WARN')
A class for waiting for Localstack to be ready.


#### exponential_backoff(exponential_backoff=None)
Get or set exponential backoff within the class.


* **Parameters**

    **exponential_backoff** (*bool**,**optional*) – If provided, set if exponential backoff is True or False.



* **Returns**

    If exponential backoff is true or false.



* **Return type**

    bool



#### localstack_endpoint(localstack_endpoint=None)
Get or set the localstack endpoint.


* **Parameters**

    **localstack_endpoint** (*str**,**optional*) – The URL of the localstack endpoint (e.g. [http://localstack:4566/health](http://localstack:4566/health)).



* **Returns**

    The URL of the localstack endpoint.



* **Return type**

    str



#### logger(logger=None)
Get or set the logger.


* **Parameters**

    **logger** (*logging.Logger*) – The logger to use for logging.



* **Returns**

    The logger to use for logging.



* **Return type**

    logging.Logger



#### maximum_retries(maximum_retries=None)
Get or set the maximum number of retries.


* **Parameters**

    **maximum_retries** (*int**,**optional*) – The maximum number of retries.  If set to zero, then will try for infinity.



* **Returns**

    The maximum number of retries.



* **Return type**

    int



#### test_interval(test_interval=None)
Get or set the interval between tests.

If exponential backoff is enabled then this number will be doubled each time
it is called.


* **Parameters**

    **test_interval** (*int**,**optional*) – Set the interval between tests or if exponential backoff is enabled, set the initial wait period.



* **Returns**

    The interval to the next test.



* **Return type**

    int



#### wait_for_all_services()
Check the health endpoint until it is successful or max attempts has been reached.


### wait4localstack.command_line_interface(args)
Process arguments provided by the command line.


* **Parameters**

    **args** (*list of str*) – The arguments to be processed.



* **Returns**

    The command line arguments provided.



* **Return type**

    args



### wait4localstack.main()
Provide an entry point for Wait4Localstack.

This is the entrypoint for the executable script that then creates and
consumes a Wait4Localstack object.

# Indices and tables


* Index


* Module Index


* Search Page
