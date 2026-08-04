print("******************* PASSWARD ****************")


correct_password = 4521
password = 0

while password != correct_password:

    password = int(input("Enter your password: "))

    if password == correct_password:
        print("Access granted")
    else:
        print("Access denied")