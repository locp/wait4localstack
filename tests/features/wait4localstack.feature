Feature: Wait4Localstack
  Scenario Outline: Test Object Methods
    Given Wait4Localstack object
    When <method> is called with <method_arguments>
    Then expect response type to be <response_type>
    And expect response value to be <response_value>
    Examples:
      | method              | method_arguments              | response_type | response_value                |
      | exponential_backoff | True                          | bool          | True                          |
      | localstack_endpoint | http://localstack:4566/health | str           | http://localstack:4566/health |
      | test_interval       | 42                            | int           | 42                            |

  Scenario Outline: Command Line Interface
    Given Wait4Localstack object
    When cli options are <cli_options>
    Then expect cli return value to match <return_value>
    Examples:
      | cli_options       | return_value |
      | --verbose         | 0            |
      | --debug --verbose | 1            |

  Scenario Outline: TestInfra
    Given sut
    When package is <testinfra_package>
    And resource is <resource_name>
    Then expect package response to match <package_response>
    Examples:
      | testinfra_package | resource_name                          | package_response |
      | file.exists       | /tmp/dist/wait4localstack-0.2.3.tar.gz | True             |
      | file.exists       | /usr/local/bin/entrypoint.sh           | True             |
      | file.exists       | /usr/local/bin/wait4localstack         | True             |
      | host.run          | /usr/local/bin/wait4localstack -h      | 0                |
      | pip.is_installed  | wait4localstack                        | True             |
