import time 
from functools import wraps

def get_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        duration = ((end_time-start_time)*10000)
        print(f"Function '{function.__name__}' took {duration:.4f} seconds to complete")
        return result
    return wrapper


# @get_time
# def linear_search_for_loop(arr, target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1

# @get_time
# def linear_search_w_enumerate(arr,target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i 
#     return -1


# array = [1,2,3,4,5,6,7,8,9,10]
# target = 7


# ß

