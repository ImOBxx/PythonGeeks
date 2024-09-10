def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar is None or x > slar:
                slar = x
    return slar

# Example usage:
my_list = [3, 5, 2, 7, 8]
print("Second largest element:", getSecMax(my_list))
