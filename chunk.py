class Chunk:
    def __init__(self, next_chunk=None):
        self.next = next_chunk

    def get_data(self):
        return self
