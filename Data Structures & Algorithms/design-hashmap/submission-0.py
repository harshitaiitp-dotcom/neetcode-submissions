class MyHashMap:
    def __init__(self):
        self.data = []
    def put(self, key, value):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))
    def get(self, key):
        for pair in self.data:
            if pair[0] == key:
                return pair[1]
        return -1
    def remove(self, key):
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data.pop(i)
                return