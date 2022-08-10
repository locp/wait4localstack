import testinfra_bdd
from wait4localstack import Wait4Localstack
from pytest_bdd import given
from pytest_bdd import scenarios

# Ensure that the PyTest fixtures provided in testinfra-bdd are available to
# your test suite.
pytest_plugins = testinfra_bdd.PYTEST_MODULES

scenarios('../features/testinfra.feature')


@given('Wait4Localstack')
def wait4localstack_object():
    """Wait4Localstack object."""
    widget = Wait4Localstack(log_level='DEBUG')
    widget.wait_for_all_services()
