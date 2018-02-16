"""
Python Basics in 2.7
"""

#variables

x = 1
fl = 5.50

boolean_true = True
boolean_false = False

string = "mystring"

#conditional statements

if x > 2:
    print("x is greater than 2")
elif 2 > x:
    print("x is less than 2")
else:
    print("x is equal to 2")

#loops

while x <= 10:
    print (str(x) + " " + "Loop 10 times")
    x += 1

for x in range(5):
    print (str(x) + " " + "Loop 5 times" )



#lists

list=["l1","l2","l3"]

for l in list:
    print(l)

print(list[1])

#tuple
tuple=(1,2,3)

for t in tuple:
    print(t)

print(tuple[0])

#dictionary
dict={"food1":"donut","food2":"sandwich","food3":"cake"}

print(dict["food2"])

for d in dict:
    print(d)

for d, value in dict.items():
    print (d, value)
