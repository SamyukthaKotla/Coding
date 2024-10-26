username = "sam"
password = "1234"

print("WELCOME")
a = input("Please enter your username: ")

if a != username:
    print("Wrong username, please enter again.")
else:
    for i in range(5):  
        b = input("Please enter the password: ")
        if b == password:
            print("Access granted.")
            break  
        else:
            print("Wrong password, please try again.")
            if i == 3:  
                print("Account blocked.")
                break