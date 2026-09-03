class MyHashSet:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    def add(self, key):
        index = key % self.size
        bucket = self.table[index]
        if key not in bucket:
            bucket.append(key)
    def remove(self, key):
        index = key % self.size
        bucket = self.table[index]
        if key in bucket:
            bucket.remove(key)
    def contains(self, key):
        index = key % self.size
        bucket = self.table[index]
        if key in bucket:
            return True
        return False