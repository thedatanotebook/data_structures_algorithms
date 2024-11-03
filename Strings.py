from timer_decorator import get_time
# String Rotation
# Do we assume the strings are the same length? 

@get_time
def string_rotate_fast(s1,s2):
    if len(s1) != len(s2):
        return -1
    concat_string = s1+s1
    answer = s2 in concat_string
    return answer

@get_time
def string_rotate_slow(s1,s2):
    if len(s1) != len(s2):
        return -1
    for i in range(len(s1)):
        r = s1[i:]+s1[:i]
        if r == s2:
            return True
    return -1


s1 = "evaporate"
s2 = "vaporatee"
print(string_rotate_fast(s1,s2))
print(string_rotate_slow(s1,s2))

