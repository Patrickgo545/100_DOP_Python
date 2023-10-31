class User:
    
    def __init__(self, user_id, username):
        # INIT - INITIALIZE WHEN CREATING AN OBJECT
        # print("new user being created...")

        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 
        self.following += 1
    


user_1 = User("001", "patrick")
# user_1.id = "001"
# user_1.username = "patrick"

print(user_1.username)

user_2 = User("002", "angela")
# user_2.id = "002"
# user_2.name = "angela"

user_1.follow(user_2)
print(user_1.following)





#################

class Car:
    def __init__(self):
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2

my_car = Car()
my_car.enter_race_mode()
print(my_car.seats)


###################