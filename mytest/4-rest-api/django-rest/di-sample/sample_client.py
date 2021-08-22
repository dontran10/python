class SampleClient(object):
    def __init__(self, config):
        self._config = config
        self.connect(self._config)

    def connect(self, config):
        # Implement function here
        print("Using config: ", config)
        print("Connected to sample service.")
