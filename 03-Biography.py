
# get user input 

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# store user input in a dictionary
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

#prints the  user information
print(user_info["name"])
print(user_info["hometown"])
print(user_info["age"])
# prints the complete dictionary