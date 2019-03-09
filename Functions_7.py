def loginCheck(show):
    print(show())

@loginCheck
def invalidDetails():
    return "Invalid User Id or Password"

@loginCheck
def sessionTimeOut():
    return "Session Time Out"

@loginCheck
def unauthorized():
    return "User is not authorized"