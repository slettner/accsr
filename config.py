from accsr.config import ConfigProviderBase, DefaultDataConfiguration
from accsr.remote_storage import RemoteStorage, RemoteStorageConfig


class __Configuration(DefaultDataConfiguration):
    @property
    def remote_storage(self):
        return RemoteStorageConfig(**self._get_non_empty_entry("remote_storage_config"))


class ConfigProvider(ConfigProviderBase[__Configuration]):
    pass


_config_provider = ConfigProvider()


def get_config(reload=False) -> __Configuration:
    """
    :param reload: if True, the configuration will be reloaded from the json files
    :return: the configuration instance
    """
    return _config_provider.get_config(reload=reload)


__remote_storage_instance = None


def default_remote_storage():
    global __remote_storage_instance
    if __remote_storage_instance is None:
        __remote_storage_instance = RemoteStorage(get_config().remote_storage)
    return __remote_storage_instance
