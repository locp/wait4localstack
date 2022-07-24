Feature: TestInfra
    Scenario Outline: Check Files
        Given the host with URL "docker://sut" is ready
        When the file is "<file_name>"
        Then the file is present
    Examples:
        | file_name                      |
        | /usr/local/bin/entrypoint.sh   |
        | /usr/local/bin/wait4localstack |

    Scenario: Check Pip Package
        Given the host with URL "docker://sut" is ready
        When the pip package is wait4localstack
        Then the pip package is present
        And the pip check is OK
    
    Scenario: Check Wait4Localstack Command
        Given the host with URL "docker://sut" is ready
        When the command is "/usr/local/bin/wait4localstack -h"
        Then the command return code is 0