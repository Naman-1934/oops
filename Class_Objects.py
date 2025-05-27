class chatbook:

    __user_id = 0

    # The __init__ method in Python is commonly referred to as a constructor. It's the special method that's automatically called 
    # when a new object (instance) of a class is created. 
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Naman'
        self.password = ''
        self.loggedin = False
        # self.menu() 

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

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