def countSwaps(a):
    # Write your code here
    container = 0
    counter = 0
    for index in range(len(a),0,-1):
        for subindex in range(len(a)-1):
            if a[subindex] > a[subindex+1]:
                container = a[subindex]
                a[subindex] = a[subindex+1]
                a[subindex+1] = container
                counter += 1
    return counter


