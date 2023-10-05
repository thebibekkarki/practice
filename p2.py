print("hello woorld")
# x=bool(5)
# print(type(x))
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# print(x + y + z)
# print(x +" " +y +" "+ z)
# x = "awesome" #gobal variable

# def myfunc():
#   print("Python is " + x)

# myfunc()
x = "awesome"  #globalvariable

def myfunc():
  x = "fantastic"  #localvariable
  print("Python is " + x)

myfunc()

print("Python is " + x)
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)