def calc(x,y,opr):
    expression = x + opr + y
    result = eval(expression)
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
x = input("Enter first number : ")
y = input("Enter second number : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}
# operations.get(ch, errHandler)(x,y)
opr = operations.get(ch)
calc(x,y,opr)