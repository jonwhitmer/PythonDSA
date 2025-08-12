# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Jon"
age = 22
gpa = 3.5
is_student = False

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(gpa)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

age = float(age)
print(age) # 22.0

age = str(age)
print(type(age)) # 22.0

name = bool(name)
print(name) # True b/c it's non-empty
print(type(name)) 
