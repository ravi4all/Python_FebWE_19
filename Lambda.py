temp = [34.5,36.7,32.1,38.4,29.6,28.7]

# cel = lambda c : 9 / 5 * c + 32
f = list(map(lambda c : 9 / 5 * c + 32, temp))

print(f)