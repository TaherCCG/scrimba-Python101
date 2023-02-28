msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg))

msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())

msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split(':'))

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(csv.split(','))


msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(' '.join(friends_list))

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))

