import time


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return

        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None


print("HASH TABLE WITH CHAINING")

# Demonstrate collision
ht = HashTable(10)

ht.insert("SKU100", "Laptop")
ht.insert("SKU001", "Mobile")

print("SKU100 Hash Index:", ht.hash_function("SKU100"))
print("SKU001 Hash Index:", ht.hash_function("SKU001"))

print("SKU100 Product:", ht.search("SKU100"))
print("SKU001 Product:", ht.search("SKU001"))

print("\n100,000 SKU LOOKUP COMPARISON")

custom_hash = HashTable(100003)
builtin_hash = {}

# Insert 100,000 SKU records
for i in range(100000):
    sku = "SKU" + str(i)
    product = "Product" + str(i)

    custom_hash.insert(sku, product)
    builtin_hash[sku] = product

search_key = "SKU99999"

# Custom hash table lookup
start = time.perf_counter()
result1 = custom_hash.search(search_key)
custom_time = time.perf_counter() - start

# Built-in dictionary lookup
start = time.perf_counter()
result2 = builtin_hash.get(search_key)
builtin_time = time.perf_counter() - start

print("Custom Hash Result:", result1)
print("Built-in Dictionary Result:", result2)

print("Custom Hash Lookup Time:", custom_time)
print("Built-in Dictionary Lookup Time:", builtin_time)

