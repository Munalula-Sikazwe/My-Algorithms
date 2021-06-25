from collections import Counter,defaultdict
def freqQuery(queries):
    c = Counter()
    d = defaultdict(set)
    for x,y in queries:
        v = c[y]
        if x==1:
            d[v].discard(y)
            d[v+1].add(y)
            c[y] = v+1
        elif x==3:
            yield 1 if d[y] else 0
        elif v:
            d[v].discard(y)
            d[v-1].add(y)
            c[y] = v-1
