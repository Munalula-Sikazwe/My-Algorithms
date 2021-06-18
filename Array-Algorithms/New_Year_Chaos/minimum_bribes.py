def minimumBribes(q):
    q = [i - 1 for i in q]  # set queue to start at 0

    bribes = 0

    for i, o in enumerate(q):

        cur = i

        if o - cur > 2:
            print("Too chaotic")

            return

        for k in q[max(o - 1, 0):i]:

            if k > o:
                bribes += 1

    print(bribes)

print(minimumBribes([1 ,2 ,5 ,3 ,4 ,7 ,8 ,6]))
