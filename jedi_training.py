print("welcome, young padawan!")
print("your jedi training begins now.")


#Math
my_int = 42
my_float = 3.14

print("The value of my_int is" , my_int)
print("The value of my_float is" , my_float)

addition = my_int + my_float
subtraction =  my_int + my_float
multiplication = my_int * my_float
division = my_int / my_float
power = my_int ** 2
modulus = my_int % 5
floor_division = my_int // 7

print("addition result:" , addition)
print("subtraction result:" , subtraction)
print("multiplication result:" , multiplication)
print("division result:" , division)
print("power result:" , power)
print("modulus result:" , modulus)
print("floor_division result:" , floor_division)

#Working with strings
first_name = "Luke"
last_name = "Skywalker"
full_name = first_name + " " + last_name
print("Your jedi name is:" , full_name)
name_length = len(full_name)
print("The lenght of your jedi name is" , name_length, "characters")
message = "May the force be with you, " + full_name + "!"
print(message)

# Starships
starships = ["Milleniium Falcon", "X-Wing", "TIE Fighter"]
print("Initial starship fleet", starships)

starships.append("star Destroyer")
print("Updated starship fleet", starships)
print("The second starship fleet is", starships[1])
print("The first starship ready for battle is", starships[0])
print("The last starship in formation is", starships[-1])

#Answer to question: I think floor division is usefull and I think it could be very useful for any program that needs rounded numbers