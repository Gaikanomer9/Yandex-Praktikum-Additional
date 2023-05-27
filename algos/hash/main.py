print(hash('hello'))  # returns some number, this will vary

print(hash('world'))  # returns some number, this will vary

print(hash('hello') == hash('hello'))  # returns True

print(hash('hello') == hash('world'))  # returns False



# Where has functions are used

my_dict = {}

my_dict['apple'] = 1
my_dict['orange'] = 2

print(my_dict['apple'])  # returns 1

# One important point to note is that not all Python objects are hashable. 
# # Immutable objects like integers, floats, strings, and tuples are hashable, 
# and thus can be used as dictionary keys. Mutable objects like lists, sets, 
# and dictionaries are not hashable, and if you try to use them as dictionary 
# keys, you'll get a TypeError.


def simple_hash(s):
    """A simple hash function for string inputs."""
    hash_value = 0
    for character in s:
        hash_value += ord(character)
    return hash_value

# Example usage:
print(simple_hash('hello'))  # returns some number
print(simple_hash('world'))  # returns some other number

# A hash function needs to satisfy two basic properties:
# 1. It should be deterministic. 
# For a given input, the output (hash) should always be the same.
# 2. Different inputs should ideally produce different outputs. 
# In practice, however, most hash functions can produce the same output for different inputs. 
# This is known as a hash collision.


def simple_mod_hash(num):
    """A simple hash function that uses modulo operator."""
    return num % 10

# Example usage:
print(simple_mod_hash(100))  # returns 0
print(simple_mod_hash(10))  # returns 0
print(simple_mod_hash(1))  # returns 1
print(simple_mod_hash(999))  # returns 9

# 0: [100, 10]
# 1: [1]
# 2: []
# 3: []
# 4: []
# 5: []
# 6: []
# 7: []
# 8: []
# 9: [999]