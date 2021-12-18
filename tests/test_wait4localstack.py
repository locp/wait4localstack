"""Wait4Localstack feature tests."""
import testinfra

from string import Template
from wait4localstack import Wait4Localstack
from wait4localstack import command_line_interface

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/wait4localstack.feature', 'Command Line Interface')
def test_command_line_interface():
    """Command Line Interface."""


@scenario('features/wait4localstack.feature', 'Test Object Methods')
def test_test_object_methods():
    """Test Object Methods."""


@scenario('features/wait4localstack.feature', 'TestInfra')
def test_testinfra():
    """TestInfra."""


@given('Wait4Localstack object', target_fixture='wait4localstack_fixture')
def wait4localstack_object():
    """Wait4Localstack object."""
    return {}


@given('sut', target_fixture='testinfra_fixture')
def sut():
    """sut."""
    return {
        'host': testinfra.get_host('docker://sut')
    }


@when('<method> is called with <method_arguments>')
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


@when('cli options are <cli_options>')
def cli_options_are_cli_options(cli_options, wait4localstack_fixture):
    """cli options are <cli_options>."""
    wait4localstack_fixture['cli_options'] = cli_options.split(' ')


@when('package is <testinfra_package>')
def package_is_testinfra_package(testinfra_package, testinfra_fixture):
    """package is <testinfra_package>."""
    testinfra_fixture['testinfra_package'] = testinfra_package


@when('resource is <resource_name>')
def resource_is_resource_name(resource_name, testinfra_fixture):
    """resource is <resource_name>."""
    with open('wait4localstack/VERSION') as stream:
        version = stream.read().strip()

    t = Template(resource_name)
    resource_name = t.substitute(VERSION=version)
    testinfra_fixture['resource_name'] = resource_name


@then('expect cli return value to match <return_value>')
def expect_cli_return_value_to_match_return_value(return_value, wait4localstack_fixture):
    """expect cli return value to match <return_value>."""
    cli_options = wait4localstack_fixture['cli_options']
    args = command_line_interface(cli_options)
    args = args.__dict__
    expected_value = int(return_value)
    actual_value = 0

    for arg in wait4localstack_fixture['cli_options']:
        arg = arg.split('-')[-1]

        if not args[arg] and expected_value == 1:
            actual_value = 1

    assert actual_value == expected_value


@then('expect package response to match <package_response>')
def expect_package_response_to_match_package_response(package_response, testinfra_fixture):
    """expect package response to match <package_response>."""
    host = testinfra_fixture['host']
    testinfra_package = testinfra_fixture['testinfra_package']
    resource_name = testinfra_fixture['resource_name']

    if testinfra_package == 'file.exists':
        expected_result = (package_response == 'True')
        actual_result = host.file(resource_name).exists
        exception_message = f'File {resource_name} does not exist.'
    elif testinfra_package == 'host.run':
        expected_result = int(package_response)
        actual_result = host.run(resource_name).rc
        exception_message = f'Run of "{resource_name}" returned {actual_result} instead of {expected_result}.'
    elif testinfra_package == 'pip.is_installed':
        expected_result = (package_response == 'True')
        actual_result = host.pip(resource_name).is_installed
        exception_message = f'Python package {resource_name} is not installed.'
    else:
        raise ValueError(f'Unknown TestInfra package {testinfra_package}')

    assert expected_result == actual_result, exception_message


@then('expect response type to be <response_type>')
def expect_response_type_to_be_response_type(response_type, wait4localstack_fixture):
    """expect response type to be <response_type>."""
    if response_type == 'bool':
        assert wait4localstack_fixture['response_type'] == bool
    elif response_type == 'str':
        assert wait4localstack_fixture['response_type'] == str
    elif response_type == 'int':
        assert wait4localstack_fixture['response_type'] == int
    else:
        raise ValueError(f'Unknown response type {response_type}.')


@then('expect response value to be <response_value>')
def expect_response_value_to_be_response_value(response_value, wait4localstack_fixture):
    """expect response value to be <response_value>."""
    assert str(wait4localstack_fixture['response_value']) == response_value
