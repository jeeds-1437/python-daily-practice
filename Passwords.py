correct_password = 'Jeevitha'
i = 1
success = False

while i<= 2:
    password = input("Enter password:")
    if password == correct_password:
        print("Login successfully!")
        success = True
        break
    else:
        print("Login Failed")
        print("Try again!!")
    i += 1
if success == False:
    print("Access denied! Too many attempts failed")
