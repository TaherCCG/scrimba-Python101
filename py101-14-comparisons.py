a = 7
b = 3
print('Comparisons')

a = 7
b = 3
print(a==b)

a = 7
b = 3
print(a!=b)

a = 7
b = 3
print(a > b)

a = 7
b = 3
print(a < b)

a = 7
b = 3
print(a>=b)

a = 7
b = 3
print(a<=b)


print('t' in 'taher')

print('t' not in 'taher')

print('m' not in 'taher')

print('m' in 'taher')

a = [3,7,42]
b = a
print(a == b)           # checks if they identical objects
print(a is b)           # checks in memory    
print(id(a), id(b))    # checks in memory if both are occupying same space in memory


a = [3,7,42]
b = [3,7,42]
print(a == b)           # returns true as they are same value
print(a is b)           # returns false as they are not identical
print(id(a), id(b))     # both have different space in memory

print(int(False))       # False value is 0
print(int(True))        # true value is 1

print(int(False))       # False value is 0
print(int(True))        # true value is 1

print(bool('Parrot'))   # boolean string with values are True
print(bool(' '))        # even if its a space
print(bool(5))          # or numbers

print(bool(''))         # empty strings are False     
print(bool(0))          # and 0 is False

print(bool([1,2]))      # list with 2 objects is True
print(bool([]))         # empty list is False

print(42 + True)        # prints 43 as True = 1
print(42 + False)       # prints 42 as False = 0

