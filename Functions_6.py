# Nested Functions
def outer():
    msg = "Output is "
    def inner_1(x,y):
        result = x + y
        return msg + str(result)
    def inner_2(x,y):
        result = x - y
        return msg + str(result)

    # print(inner_1(12,4))
    # print(inner_2(4,1))
    return inner_1, inner_2

# x = outer()
# print(x)

# add, sub = outer()
# print(add(3,6))

print(outer()[0](5,8))