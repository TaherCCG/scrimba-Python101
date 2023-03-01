print("Return Statements")

# functions below calculates tax
# each function returns something different
# due to what i put in return statement

#this function returns none
def value_added_tax(amount):
    tax = amount * 0.25
    
print(value_added_tax(100))       # prints none. as the function has no return statement

# this function returns calculate tax as i have returned tax1
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax                         # returns tax
    
print(value_added_tax(100))            # prints calculated tax as thats what is returned

# this function returns few values
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return tax,amount                  # returns tax and amount
    
price=value_added_tax(100)             #  calculated tax and type
print(price, type(price))              # prints price and data type as tuple

# this function returns few values
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [tax,amount,total_amount]   # returns tax, amount and total_amount as list because of square brackets []
    
price=value_added_tax(100)             # calculated tax and type
print(price, type(price))              # prints price and data type as List

# this function returns few values
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return {tax,amount,total_amount}   # returns tax, amount and total_amount as set because of curly brackets {}
    
price=value_added_tax(100)             # calculated tax and type
print(price, type(price))              # prints price and data type as set

# this function returns few values
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{tax,amount,total_amount}"   # returns tax, amount and total_amount as string
    
price=value_added_tax(100)             # calculated tax and type
print(price, type(price))              # prints price and data type as string