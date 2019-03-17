import readWrite

def login():
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    users = readWrite.readData()
    print(users)
    for user in users:
        # if user[1] == email and user[2] == pwd:
        if email in user and pwd in user:
            print("Welcome",user[0])
            break
    else:
        print("Not registered...")

def register():
    name = input("Enter your name : ")
    users = readWrite.readData()
    while True:
        email = input("Enter your email : ")
        for i in range(len(users)):
            if email in users[i]:
                print("Email Id already exist")
                break
        else:
            break

    pwd = input("Enter your password : ")
    user = {'name':name,'email':email,'pwd':pwd}
    print(user)
    readWrite.writeData(user)

while True:
    print("""
    1. Login
    2. Register
    """)

    ch = input("Enter your choice : ")

    todo = {
        "1" : login,
        "2" : register
    }
    todo.get(ch)()