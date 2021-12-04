st = 'adaecbdc'

def longestPalindrome_bad(st):
    count = 0
    freq = [0 for i in range(26)]
    for i in st:
        freq[ord(i) - ord('a')] += 1
    for i in freq:
        if(i%2 == 0):
            count += i
        else:
            count += i-1
    return count + 1

def longestPalindrome_good(st):
    count,flagOddValue = 0,False
    freq = [0 for i in range(26)]
    for i in st:
        freq[ord(i) - ord('a')] += 1
    for i in freq:
        if(i%2 == 0):
            count += i
        else:
            flagOddValue = True
            count += i-1
    if (flagOddValue):
        return count + 1
    else:
        return count

try:
    if st.isalpha():
        print(longestPalindrome_good(st) != longestPalindrome_bad(st))
    else:
        print(False)
    except:
        print(False)