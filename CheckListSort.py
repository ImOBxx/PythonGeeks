l = [10, 20, 30, 15, 40]
is_sorted = True
for i in range(1, len(l)):
    if l[i] < l[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("Yes")
else:
    print("No")
