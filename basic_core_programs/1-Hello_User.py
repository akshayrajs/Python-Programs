#User Input and Replace String Template “Hello <<UserName>>, How are you?


while True:
    try:
        username=input("Enter the username : ")
        if len(username)>=3:
            break
        else:
            print("Error : Username should have minimum 3 characters.")
    except:
        print("Wrong Input")

print(f"Hello {username}, How are you?")