# CONSTRUCT WORD

memo = {}

def constructWord(word,wordlist):
    if word == '':
        return [[]]
    if word in memo.keys():
        return memo[word]
    totalWordList = []
    for subword in wordlist:
        if subword == word[:len(subword)]:
            subwordlist = constructWord(word[len(subword):],wordlist)
            totalWordList.extend([[subword] + lst for lst in subwordlist])
    memo[word] = totalWordList
    return totalWordList