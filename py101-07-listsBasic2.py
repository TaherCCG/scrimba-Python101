friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
# sort list
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
cars.sort()
print(cars)

#min max sum
print(min(cars))
print(max(cars))
print(sum(cars))
print(min(friends)) #prints lowest in list of alphabetical order
print(max(friends)) #prints highest in list of alphabetical order


friends.append('TerryG')  #adds friend to list
friends.insert(0,'TerryG')
friends[2]='Trigz'

friends.extend(cars)

friends.remove('TerryG')
friends.pop(2)
#friends.clear()
del friends[4]

new_friends = list(friends)
print(friends)
print(new_friends)

print(friends)

