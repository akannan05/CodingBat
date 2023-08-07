# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
    x = ""
    for i in range(n):
        x += str
    return x

# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
# or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    x = ""
    front = ""
    if len(str) < 3:
        front = str
    else:
        front = str[0:3]
    for i in range(n):
        x += front
    return x

# Given a string, return a new string made of every other char starting with the first, 
# so "Hello" yields "Hlo".
def string_bits(str):
    x = ""
    for i in range(0, len(str), 2):
        x += str[i]
    return x

# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    x = ""
    for i in range(0, len(str)+1):
        x += str[0:i]
    return x

# Given a string, return the count of the number of times that a substring length 2 appears in the 
# string and also as the last 2 chars of the string, so "hixxxhi" yields 1 
# (we won't count the end substring).
def last2(str):
    count = 0
    l2 = str[len(str)-2:]
    for i in range(len(str)-2):
        if str[i:i+2] == l2:
            count += 1
    return count

# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] == 9:
            count += 1
    return count

# Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
# The array length may be less than 4.
def array_front9(nums):
    ans = False
    for i in range(0, len(nums)):
        if i >= 4:
            return False
        if nums[i] == 9:
            return True
    return ans

# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    ans1 = False
    ans2 = False
    ans3 = False
    for i in range(0, len(nums)):
        if nums[i] == 1:
            ans1 = True
        if nums[i] == 2:
            ans2 = True
        if nums[i] == 3:
            ans3 = True
    if ans1 and ans2 and ans3 == True:
        return True
    return False

# Given 2 strings, a and b, return the number of the positions where they contain the same length 
# 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear 
# in the same place in both strings.
def string_match(a, b):
    count = 0
    for i in range(0, len(a)-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count