# def temp_conv(c):return 9/5 * c + 32
# print(temp_conv(34.4))

temperatures = [34.5,26.7,37.6,29.6,32.1]
f = list(map(lambda c : 9/5 * c + 32, temperatures))
print(f)