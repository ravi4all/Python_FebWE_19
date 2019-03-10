def temp_conv(c):
    return 9/5 * c + 32

# f = temp_conv(34.5)
# print(f)
temperatures = [34.5,26.7,37.6,29.6,32.1]
# f = []
# for t in temperatures:
#     # print(temp_conv(t))
#     f.append(temp_conv(t))
# print(f)

# f = list(map(temp_conv, temperatures))
# print(f)

def myMap(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = myMap(temp_conv, temperatures)
print(f)