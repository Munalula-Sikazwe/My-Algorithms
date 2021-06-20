def makeAnagram(a, b):
    # Write your code here
    count = 0
    letters = defaultdict(int)
    for letter in a:
        if letter not in b  :
            a = a.replace(letter,'',1)
            count += 1
    for letter in b:
        if letter not in a :
            b = b.replace(letter,'',1)
            count += 1
    for letter in a:
         if a.count(letter) != b.count(letter) :
            letters[letter] += 1
    print(letters)
    for letter in letters:
        count += 1
    return count