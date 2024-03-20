import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from test_factories import UserFactory
from django.core.management import call_command

print("LOADED CONFIG")


@pytest.fixture(scope='session')
def initialize_test_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('populate_products')


@pytest.fixture
def client():
    return APIClient()


register(UserFactory)
