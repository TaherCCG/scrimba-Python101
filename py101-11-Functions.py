print("Function")

#Simple function takes name and age as arguments from user and prints name and age
def greeting(name,age=int):
    print(f"Hello {name}, you are {age}!")
    
name=input("Enter your name:")
age=input("How old are you?:")
greeting(name,age)
