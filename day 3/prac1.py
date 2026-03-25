name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hello {}, you are eligible to vote.".format(name))
else:
    print("Hello {}, you are not eligible to vote.".format(name))
