#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    string = ""
    for i in range(len(str)):
        string += str[i]+str[i]
    return string

#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count

#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            cat += 1
        if str[i:i+3] == "dog":
            dog += 1
    return cat==dog

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and 
# "cooe" count.
def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3:i+4] == "e":
            count += 1
    return count

#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences 
# (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a,b):
    a2 = a.lower()
    b2 = b.lower()
    return a2.endswith(b2) or b2.endswith(a2)

#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but 
# "x.xyz" does not.
def xyz_there(str):
    bool = False
    for i in range(len(str)-2):
        if str[i:i+3] == "xyz":
            bool = True
            if i>1:
                if str[i-1:i] == ".":
                    bool = False
    return bool



    