class chatbook:
    def __init__(self):
        self.surname = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook || How would like to proceed?
                           1. press 1 for signup
                           2. press 2 for signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username: ")
            pwd = input("Enter your password: ")
        if uname == self.username and self.password == pwd:
            print("You have signed in successfully")
            self.loggedin = True
        else:
            print("Invalid username or password")
        print("\n")
        self.menu()



obj = chatbook()