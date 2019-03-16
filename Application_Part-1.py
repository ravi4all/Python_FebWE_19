users = []
def login():
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    for user in users:
        if user['email'] == email and user['pwd'] == pwd:
            print("Welcome",user['name'])
            break
    else:
        print("Not registered...")

def register():
    name = input("Enter your name : ")
    while True:
        email = input("Enter your email : ")
        for i in range(len(users)):
            if users[i]['email'] == email:
                print("Email Id already exist")
                break
        else:
            break

    pwd = input("Enter your password : ")
    user = {'name':name,'email':email,'pwd':pwd}
    users.append(user)
    print(user)

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