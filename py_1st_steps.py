print("Hello, World!")

# Variables creation & printing it
age = 23
price = 19.37
first_name = "josh"
is_online = True  # py is case sensitive true not the same as True
print(age)

#exercise from video
name = "John Smith"
age = 20
new_patient = True


#receive input
#------------------------------------------
name = input("What is your name? ")

print("Hello " + name)

#type conversion
#------------------------------------------
birth_year = input("In which year were you born? ")
age = 2026 - int(birth_year)    # input returns strig which we can't subtract from an integer

print(age)     #integer = full number    int() 
               #float = decimal number   float()
               #boolean = True or False  bool()
               #string = text            str()
#exercise from video "lil calculator
First_number = input("Please choose the first number you want to add:                                 \
                     First number: ")
second_number = input("Second number: ")
result = float(First_number) + float(second_number)
print(result)