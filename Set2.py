l = [10, 20, 3, 4, 10, 20, 7, 3]
r1 = {x for x in l if x % 2 == 0}
r2 = {x for x in l if x % 2 != 0}
print(r1)
print(r2)