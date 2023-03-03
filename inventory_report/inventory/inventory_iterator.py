class InventoryIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item
