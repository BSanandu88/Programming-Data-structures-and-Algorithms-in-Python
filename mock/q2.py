""" The given function LongestOddNumber(st) accepts a string st containing only digits that
represents a number (for e.g. st ="3876" represents the number 3876 ), and returns the longest
substring of st that represents an odd number, if no such substring exists return an empty
string. For e.g. when st ="3876" substring representing longest odd number is "387". """

from _typeshed import ReadableBuffer


st = '3876'

# Suffix

def LongestOddNumber_good(st):
    flag = False
    n = len(st) - 1
    for i in range(n,-1,-1):
        val = (int)(st[i])
        if(val % 2 != 0):
            flag = True
            break
    if(flag):
        return st[:i+1]
    else:
        return ""

def LongestOddNumber_bad(st):
    count = 0
    n = len(st) - 1
    for i in range(n,-1,-1):
        count += 1
        val = (int)(st[i])
        if(val%2 != 0):
            break
    return st[:i+1]

try:
    print(LongestOddNumber_good(st) != LongestOddNumber_bad(st))
except:
    print(False)