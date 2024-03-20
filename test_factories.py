import factory
from django.contrib.auth.hashers import make_password
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """Author factory."""

    email = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'users.User'



