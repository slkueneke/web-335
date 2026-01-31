#variables
age = 20
price = 19.95
first_name = 'Shannon'
is_online = True #case sensitive, booleans need a capital first letter
print(age)

#strings
course = 'Python for Beginners'
print(course.upper()) #returns new string does not change og string
print(course.find('y')) #case sensitive; returns index
print(course.replace('for', '4')) #immutable - does not change og string, returns a new string
print ('Python' in course) #returns boolean, not index

#arithmetic operators
print(10 + 3) # also -, *, % (returns remainder)
print(10 / 3) #returns float
print(10 // 3) #returns whole number
print(10 ** 3) #10 to the power of 3 = 1000. (10*10*10)

#augmented assignment operator: +=, -=, *=, /=
