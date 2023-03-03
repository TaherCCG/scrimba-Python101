print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

# write a while loop to print same as above

# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5

i=0
while i < 5:
    i=i+1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
    if i == 5:
        print ("Python Rocks!")

