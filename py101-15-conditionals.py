print("Conditionals: IF statements\n")

# practising on if statements with elif and else statements 
# changing booleans to true or false to get different results.

#raining is true
is_raining = True           
print("Good Morning")
if is_raining:
    print("Its raining, Bring Umbrella")
else:
    print("It's a nice day today")


# its raining or its cold
is_cold=True
is_raining = True
print("Good Morning")
if is_raining or is_cold:
    print("Bring Umbrella or a jacket")
else:
    print("It's a nice day today")

#its raining and its cold
is_cold=True
is_raining = True
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and a jacket its cold too")
else:
    print("It's a nice day today")

#its raining and its cold
is_cold=True
is_raining = True
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and a jacket its cold too")
elif is_raining and not(is_cold):
    print("Its raining Bring Umbrella!")
elif not(is_raining) and (is_cold):
    print("Its cold Bring Jacket!")
else:
    print("It's a nice day today")

#its raining and its not cold
is_cold=False
is_raining = True
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and a jacket its cold too")
elif is_raining and not(is_cold):
    print("Its raining Bring Umbrella!")
elif not(is_raining) and (is_cold):
    print("Its cold Bring Jacket!")
else:
    print("It's a nice day today")    

#its cold and its not raining
is_cold=True
is_raining = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and a jacket its cold too")
elif is_raining and not(is_cold):
    print("Its raining Bring Umbrella!")
elif not(is_raining) and (is_cold):
    print("Its cold Bring Jacket!")
else:
    print("It's a nice day today")

#Its a nice day
is_cold=False
is_raining = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and a jacket its cold too")
elif is_raining and not(is_cold):
    print("Its raining Bring Umbrella!")
elif not(is_raining) and (is_cold):
    print("Its cold Bring Jacket!")
else:
    print("It's a nice day today!")
