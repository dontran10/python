from dependency_injector import providers, containers
from sample_client import SampleClient
from sample_reader import SampleReader


class MyConfigs(containers.DeclarativeContainer):
    config = providers.Configuration('config')


class MyClients(containers.DeclarativeContainer):
    client = providers.Singleton(SampleClient, MyConfigs.config)


class MyReaders(containers.DeclarativeContainer):
    reader = providers.Factory(
        SampleReader,
        client=MyClients.client
    )
