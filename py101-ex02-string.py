#Python 101: String Exercise 1
# 1. From the string "Welcome to Python 101: Strings", extract text and create
#    print new string that says: 
# - "1 Welcome Ring To Tyler" 
# - Every 1st letter in a word should be capitalized (title format)
# 2. Print same string backwards

msg=("Welcome to Python 101: Strings")


msg1=msg[18]+" "+msg[0:8]+msg[-5:-1]+msg[7:11]+msg[-6]+msg[12]+msg[2]+msg[1]+msg[-5]


print(msg)
print(msg1.title())

print(msg[::-1].capitalize())
print(msg1[::-1].title())


print("hello world".title())