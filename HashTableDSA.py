'''
Hash map is nothing but a dictionar data type in python.
The below code provides the deep understanding about the dictionary.

Data: Thursday, October 6, 2022
Name: Bishal jaiswal

'''
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    # function to generate the hash from the given key
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # function to add the key and value hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    # function to fetch the price of the stocks in the given months
    def __getitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                return self.arr[h][index][1]
            else:
                return "Key not found!"

    # function to remove the stock from the hash table
    def __delitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                del self.arr[h]
                return
            else:
                return "Key not found!"


if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = 1000
    ht["march 17"] = 2000
    del ht["march 17"]
    print(ht.arr)
