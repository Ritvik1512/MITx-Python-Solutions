__author__ = 'Ritvik Choudhary'

# Week1 - Lecture 1 and 2.

# The following is a stratight line program, hence it's completes in constant time, i.e. time depends only on the length of the program.
# Surface area of a sphere.

radius = 14
pi = 3.14

area = 4*pi*(radius**2)

print(area)

radius= 13 # Even after changing the radius, the area doesn't change because it has been binded to a particular value already.
print(radius)

####################

#We can do stuff with strings as well
a = 'helloworld \n'
print(a[1::2])

b="This is a python code"
print(a+b)
##Using raw_input
y = raw_input("What's up?")
print(y**2)

# Below is a branching program(We need branching programs in python)
a = 'abc'
print(type(a))


# L2 PROBLEM 8:
str1 = 'hello'
str2 = 'world'

str3 = str1+' '+str2
print(str3)

# L2 PROBELM 10:
if happy>2:
   print('hello world')

# L2 PROBLEM 11:
if type(varA) == str or type(varB) == str:
    print("string involved")

elif varA > varB:
    print("bigger")

elif varA == varB:
    print("equal")

elif varA < varB:
    print("smaller")

else:
    print("We are done")

print("end")