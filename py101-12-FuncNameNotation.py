print("Functions Named Notation")

def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if available, default age is used   
   #print("Hello "  +  name.capitalize() + ", you will be " + str(age+1) +" next birthday!")
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

#greeting("brian", 27,"Blue")
greeting(age=27, name="brian",color="Blue") # different order to above line, but arguments make them match 

#example
#       Profile(1995,83.5,192,"blue")     is not readable, might not be able to tell what arguments mean
#       Profile(yob=1995,weight=83.5,height=192,eye_color="blue")    is readable and can tell what each argument is

