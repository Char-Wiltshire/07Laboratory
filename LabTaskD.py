password = "admin123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Access denied. You have {max_attempts - attempts} attempts left.")