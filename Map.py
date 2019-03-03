def cel(c):
    return 9/5 * c + 32

# f = cel(45.4)
# print(f)
temp = [34.5,36.7,32.1,38.4,29.6,28.7]
f = list(map(cel, temp))
print(f)