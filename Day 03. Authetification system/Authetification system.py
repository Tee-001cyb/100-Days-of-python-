user_info = {}
def register_user():
     username = input("Enter your username: ").lower()
     if username in user_info:
          print("username already exist please choose a different name")
     else:
          password = input("Enter a password: ").lower()
          user_info[username] = password
          print("registertion successful")

def login_user():
     username = input("Enter your username: ").lower()
     password = input("Enter your password: ").lower()

     if username in user_info and user_info[username] == password:
          print(f"welcome back, {username}")
     else: 
          print("Invalid username or password")

def authentification():
   while True:
     print("Basic Authentification System")
     print("1. Register")
     print("2. Login")
     print("3. Exit")
     
     option = input ("enter the next action: ").lower()
     if option == "1":
          register_user()
     elif option == "2":
          login_user()
     elif option == "3":
          print("Exiting this page")
          break
     else:
          print("Enter the option given above")

authentification()