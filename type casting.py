# type casting using for converting one data type to another data type 

name= "safeela"
age= 22
gpa= 3.5
is_student= True

print(type(name))    # <<< it is using to know which data type it is
print(type(age))
print(type(gpa))
print(type(is_student))

age=float(age)   # here changing data type int to float
gpa=int(gpa)   # here changing data type string into int


print(type(gpa))   #here it print the type of gpa
print(type(age))
print(type(name))