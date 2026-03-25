a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("Before swapping: a={} b={}".format(a, b))
a = a + b
b = a - b
a = a - b
print("After swapping: a ={} b={}".format(a, b))
