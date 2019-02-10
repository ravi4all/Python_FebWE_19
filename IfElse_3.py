msg = input("Enter your message: ")

helloIntent = ['hi','hey','hello','howdy','hello there','hi there']
timeIntent = []
dateIntent = []

for intent in helloIntent:
    if intent == msg:
        print("Hello User")
for intent in timeIntent:
    if intent == msg:
        print("Hello User")
for intent in dateIntent:
    if intent == msg:
        print("Hello User")


# if msg == 'hello':
#     print('Hello User')
# elif msg == 'bye':
#     print('Bye User')
# else:
#     print("I donot understand")