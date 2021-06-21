def plusMinus(arr):
    # Write your code here
    total = len(arr)
    numbers = defaultdict(int)
    for number in arr:
        if number > 0:
            numbers['positive'] += 1
        elif number < 0:
            numbers['negative'] += 1
        else:
            numbers['zero'] += 1
    print(format(numbers['positive']/total,".6f"))
    print(format(numbers['negative']/total,".6f"))
    print(format(numbers['zero']/total,".6f"))