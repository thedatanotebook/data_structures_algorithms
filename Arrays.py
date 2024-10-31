from timer_decorator import get_time
import random

@get_time
def contains_duplicate_hash(arr):
    # A set is a built in data type that creates a set, in an unordered collection of unique elements. Mutable, efficient time complexity.
    # Hash table 
    duplicates = {}
    for i in arr:
        if i in duplicates:
            return True 
        else:
            duplicates[i] = 1 
    return False

# We used a dictionary to keep track of items. A Hash Table provides average of O(n) time complexity. Checking if an item is already in dictionary is quick. Dynamic Storage allows python dictionaries to resize. 


@get_time
def contains_duplicate_less(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]: 
                return True
    return False

# Nested Loops iterates through each element 
# Outer Loop iterates through each element of the arry and the inner loop checks for the subsequent. 
#   O(n^2)


arr = [random.randint(1,100) for i in range(100)]

print(contains_duplicate_hash(arr))
print(contains_duplicate_less(arr))


# results = 
    # Function 'contains_duplicate_hash' took 0.0095 seconds to complete
    # True
    # Function 'contains_duplicate_less' took 0.0405 seconds to complete
    # True


