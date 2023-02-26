failed_subjects="2"
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print('{}  will need to redo {} courses.'.format(name,failed_subjects))
name="Eric"
print(f"{name} is doing well in geography.\n")
print()

msg = "I love Python"
   
# Printing the center aligned 
print ("Center aligned string is: ")
print (msg.center(40, ' '))
 
# Printing the left aligned 
print ("The left aligned string is: ")
print (msg.ljust(40, ' '))
 
# Printing the right aligned string
print ("The right aligned string is : ")
print (msg.rjust(40, ' '))

print()

# Printing different order
print('{0} and {1}'.format('one', 'two'))
print('{1} and {0}'.format('one', 'two'))

print()

""" Passing an integer after the ':' will cause 
that field to be a minimum number of characters wide. 
This is useful for making columns line up.
"""
table = {'scrimba': 4127, 'Python': 4098, 'Taher': 7678}
for name, phone in table.items():
    print(f'{name:15} ==> {phone:15d}')

    
