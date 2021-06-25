def twoStrings(s1, s2):
    if s1 == '' or s2 == '':
        return "No"
    else:
        for letter in s1:
            if letter in s2:
                return "YES"
        return "NO"
