class SampleReader(object):
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e

    def read(self):
        # Implement function here
        print("Sample reader - read action")
