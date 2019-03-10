def even(n):
    return n % 2 == 0

# print(even(5))
# numbers = []
# for i in range(100):
#     numbers.append(i)

numbers = [i for i in range(100)]
# e = []
# for num in numbers:
#     if even(num):
#         e.append(num)
# print(e)
e = list(filter(even, numbers))
print(e)