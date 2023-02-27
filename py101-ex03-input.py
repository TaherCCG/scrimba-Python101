# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('Enter your name: ')
dist_km = input('Enter distance in km: ')
dist_mi = float(dist_km)/1.609
print(f'Hi {name.title()}! {dist_km}km is equivalent to {round(dist_mi,1)} miles.')