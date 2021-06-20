from collections import Counter
def makeAnagram(s1, s2):
    return len(s1)+len(s2)-sum((Counter(s1) & Counter(s2)).values())*2
## number of deletions = sum of  length of strings - sum of length of intersecting values frequency.
string1 = "abcc"
string2 = "cdecc"
print(Counter(string1))
print(Counter(string2))
print(Counter(string1)& Counter(string2))
