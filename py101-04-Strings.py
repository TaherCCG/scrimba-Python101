msg='welcome to Python 101: Strings'
print(msg)
print(msg+msg)
print(msg,msg)
print (msg*1)
print (msg.upper())
print (msg.lower())
print (msg.capitalize())
print (msg.title())
print (len(msg))
print (msg.count('Python'))
print (msg.count('o'))

#slicing
print(msg[0])
print(msg[5])
print(msg[0:7])
print(msg[10:-13])
print(msg[10:17])
print(msg[18:21])

msg3="""
#slicing as shown above
print(msg[0])
print(msg[5])
print(msg[0:7])
print(msg[10:-13])
print(msg[10:17])
print(msg[18:21])
"""
print (msg3)

# find & replace
print(msg.find("P"))
print(msg.replace("Python","HTML"))
msg4=msg.replace("Python","Java")
print (msg4)

print("Python" in msg)
print("Python" not in msg)

#formatted string
name='TRIGZ'
color = 'PURPLE'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
msg2 = '{} loves the color {}!'.format(name.capitalize(),color.lower()) 
print(msg)
print(msg1)
print(msg2)