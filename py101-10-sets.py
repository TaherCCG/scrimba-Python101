#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']                    #list
friends_tuple = ('John','Michael','Terry','Eric','Graham')              #tuple cant change
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}         #set cant have duplicates
print(friends)
print(friends_tuple)
print(friends_set)
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}              #2nd set

print('exists in both sets :',friends_set.intersection(my_friends_set))  # finds who exists in both sets
print(friends_set & my_friends_set)                                      # Same as above but use &

print('difference in set : ',friends_set.difference(my_friends_set))     # difference in both sets
print(friends_set - my_friends_set)                                      # same as above uses minus sign

print('puts both sets together:',friends_set.union(my_friends_set))      # puts both sets together
print(friends_set | my_friends_set)                                      # pipe is same as union

print('shows all unique  :',friends_set.symmetric_difference(my_friends_set)) # shows all unique chars from each set (no doubles that exist in both)
print(friends_set ^ my_friends_set)                                           # same as above use ^ 


#Sets - blazing fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()