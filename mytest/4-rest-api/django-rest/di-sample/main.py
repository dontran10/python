from containers import MyReaders, MyClients, MyConfigs


# Ref: https://github.com/ets-labs/python-dependency-injector
if __name__ == "__main__":
    MyConfigs.config.override({
        "name": "sample-config",
    })

    reader = MyReaders.reader()
    reader.read()
