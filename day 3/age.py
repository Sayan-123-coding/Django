name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age <= 5:
    print("Hello {}, you are a kid.".format(name))
elif age <= 11:
    print("Hello {}, you are a child.".format(name))
elif age <= 19:
    print("Hello {}, you are a teenager.".format(name))
elif age <= 59:
    print("Hello {}, you are an adult.".format(name))   
else:
    print("Hello {}, you are a senior citizen.".format(name))
        