print ()
l = [10, 20, 30, 40, 50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])
print ()

l.append(30)
print(l)
l.insert(1, 15)
print(l)
print(15 in l)
print(l.count(30)) #count 30 in list
print(l.index(30))
print(l.index(30, 4, 7)) #search Index

