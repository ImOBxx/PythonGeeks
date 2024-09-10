s = "geeksforgeeks"
l1 = [x for x in s if x in "aeiou"]
print(l1)

l2 = ["geeks", "ide", "courses", "gfg"]
l3 = [x for x in l2 if x.startswith("g")]
print(l3)

l4 = ["geeks", "for", "geeks", "gfg", "ide"]
l5 = [x.upper() for x in l4 if x.startswith("g")]
