"""Wait4Localstack feature tests."""

from wait4localstack import Wait4Localstack
from wait4localstack import command_line_interface

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)


scenarios('../features/wait4localstack.feature')


@given('Wait4Localstack object', target_fixture='wait4localstack_fixture')
def wait4localstack_object():
    """Wait4Localstack object."""
    return {}


@when(parsers.parse('{method} is called with {method_arguments}'))
def method_is_called_with_method_arguments(method, method_arguments, wait4localstack_fixture):
    """<method> is called with <method_arguments>."""
    wait4localstack_fixture['method'] = method
    widget = Wait4Localstack()

    if method == 'exponential_backoff':
        b = (method_arguments == 'True')
        widget.exponential_backoff(b)
        response = widget.exponential_backoff()
    elif method == 'localstack_endpoint':
        widget.localstack_endpoint('http://localstack:4566/health')
        response = widget.localstack_endpoint()
    elif method == 'test_interval':
        i = int(method_arguments)
        widget.test_interval(i)
        response = widget.test_interval()
        widget.exponential_backoff(True)
        i = widget.test_interval()
    else:
        raise ValueError(f'Unknown method {method}.')

    wait4localstack_fixture['response_value'] = response
    wait4localstack_fixture['response_type'] = type(response)


@when(parsers.parse('cli options are {cli_options}'))
def cli_options_are_cli_options(cli_options, wait4localstack_fixture):
    """cli options are <cli_options>."""
    wait4localstack_fixture['cli_options'] = cli_options.split(' ')


@then(parsers.parse('expect cli return value to match {return_value:d}'))
def expect_cli_return_value_to_match_return_value(return_value, wait4localstack_fixture):
    """expect cli return value to match <return_value>."""
    cli_options = wait4localstack_fixture['cli_options']
    args = command_line_interface(cli_options)
    args = args.__dict__
    expected_value = return_value
    actual_value = 0

    for arg in wait4localstack_fixture['cli_options']:
        arg = arg.split('-')[-1]

        if not args[arg] and expected_value == 1:
            actual_value = 1

    assert actual_value == expected_value


@then(parsers.parse('expect response type to be {response_type}'))
def expect_response_type_to_be_response_type(response_type, wait4localstack_fixture):
    """expect response type to be <response_type>."""
    response_types = {
        'bool': bool,
        'str': str,
        'int': int
    }

    if response_type not in response_types:
        raise ValueError(f'Unknown response type {response_type}.')

    assert wait4localstack_fixture['response_type'] == response_types[response_type]


@then(parsers.parse('expect response value to be {response_value}'))
def expect_response_value_to_be_response_value(response_value, wait4localstack_fixture):
    """expect response value to be <response_value>."""
    assert str(wait4localstack_fixture['response_value']) == response_value
