password = "admin123"

while True:
    password = input("Enter the password: ")
    if password == "admin123":
        print("Access granted")
        break
    else:
        print("Access denied")
        