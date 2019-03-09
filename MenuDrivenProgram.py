def add(x,y):
    result = x + y
    print(result)
def sub(x,y):
    result = x - y
    print(result)
def div(x,y):
    result = x / y
    print(result)
def mul(x,y):
    result = x * y
    print(result)

def errHandler(*args):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations.get(ch, errHandler)(x,y)