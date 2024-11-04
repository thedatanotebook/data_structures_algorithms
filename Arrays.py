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
# Outer Loop iterates through each element of the arry and the inner loop checks 
# for the subsequent. 
#   O(n^2)


arr = [random.randint(1,100) for i in range(100)]

print(contains_duplicate_hash(arr))
print(contains_duplicate_less(arr))
print(f"\n")


# results = 
    # Function 'contains_duplicate_hash' took 0.0095 seconds to complete
    # True
    # Function 'contains_duplicate_less' took 0.0405 seconds to complete
    # True



#### CHECK UNSCRAMBLING

# We would want to check each array to see if there are duplicates in another hash table. 
# The bad way would be to loop through string one then count each occurance of a character
#     in both strings while looping through the first string.

# First solution would be this: 

@get_time
def isScrambled(s, t):
    if len(s) != len(t):
        return -1 
    
    for letter in s:
        c1 = 0 
        c2 = 0

        for l in s: 
            if l == letter:
                c1 += 1

        for l in t:
            if l == letter:
                c2 += 1 

    if c1 == c2:
        return True  
    
    return False


# The better approach is to use memory and store the counts in a hash table
@get_time
def isScrambled_improved(s,t):
    if len(s) != len(t):
        return -1
    
    letter_count = {}

    for l in s:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1

    for l in t:
        if l in letter_count:
            letter_count[l] -= 1
        else:
            return False
    

    for l in letter_count.values():
        if l != 0:
            return False

    return True 

s1 = "forgiveness"
s2 = "givessnrofe"

print(isScrambled(s1,s2))
print(isScrambled_improved(s1,s2))

@get_time
def two_sum_slow(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] +arr[j] == target:
                return True
    return -1

@get_time
def two_sum_fast(arr, target):
    sum_val = {}
    for i, value in enumerate(arr):
        if value in sum_val:
            return [i, sum_val[value]]
        else:
            sum_val[target-value] = i
    return -1


print(two_sum_slow([1,2,3,4,5], 8))
print(two_sum_fast([1,2,3,4,5], 8))









        



