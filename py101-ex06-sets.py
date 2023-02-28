#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1
print('Eric' in friends and 'John' in friends)
#2
print(friends | my_friends)                          
#3
print(friends & my_friends) 
#4
print(friends - my_friends)
#5
print(friends ^ my_friends)
#6
cars_no_dupl =set(cars)
print(cars_no_dupl)