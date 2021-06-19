from collections import defaultdict
def checkMagazine(magazine, note):
    # Write your code here
    new_magazine = defaultdict(int)
    for word in magazine:
        new_magazine[word] += 1
    for word in note:
        new_magazine[word] -= 1
    for word in new_magazine :
        if new_magazine[word] < 0:
            print("No")
            return
    print("Yes")