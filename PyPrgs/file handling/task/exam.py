def register():
    username = input("Please input the first 2 letters of your first name and your birth year ")
    password = input("Please input your desired password ")
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("You are now logged in...")
    else:
        print("You aren't logged in!")

def login():
    username = input("Please enter your username")
    password = input("Please enter your password")  
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
login()
register()
