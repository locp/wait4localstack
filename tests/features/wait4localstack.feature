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
