from collections import defaultdict, Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    container = []
    frequency = defaultdict(int)
    for operation, value in queries:
        frequency = Counter(container)
        if operation == 1:
            container.append(value)
        if operation == 2:
            if value in container:
                container.remove(value)
        if operation == 3:
            if value in frequency.values():
                output.append(1)
            else:
                output.append(0)

    return output