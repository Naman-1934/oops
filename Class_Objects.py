class chatbook:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook || How would like to proceed?
                           1. press 1 for signup
                           2. press 2 for signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit
                           -> """)
                           
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg_friend()
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

    def my_post(self):
        if self.loggedin == True:
            post = input("Enter your post: ")
            print(f"Your post {post} has been posted successfully")
        else:
            print("You need to sign in first to post")
        print("\n")
        self.menu()

    def sendmsg_friend(self):
        if self.loggedin == True:
            msg = input("Enter your message -")
            frd = input("Whom do you want to send the message to? ")
            print(f"Your message {msg} has been sent to {frd} successfully")
        else:
            print("You need to sign in first to send a message")
        print("\n")
        self.menu()




obj = chatbook()