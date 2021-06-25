def alternatingCharacters(s):
    # Write your code here
    count = 0
    new_string = ''
    for index in range(len(s) - 1):
        if s[index] == s[index + 1]:
            count += 1

    return count
