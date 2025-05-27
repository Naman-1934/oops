from Class_Objects import chatbook

user = chatbook()
# print(user.id)

# When you write a code like this: self.__name = 'Naman' then you have to write this code to show an output: self.__name = self.__class__.__name
# print(user.__name)


### Getter and Setter Method

# print(user.get_name())
# user.set_name('Agent Naman')
# print(user.get_name())


### Static Method

user1 = chatbook()
print(user1.id)

chatbook.set_id(27)
user2 = chatbook()
print(user2.id)  

user3 = chatbook()
print(user3.id)