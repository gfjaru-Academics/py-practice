def hello(): ## generic function
    print("Hi!")

def greet(name, greeting = "Hi"): # variable, + with default value
    print(greeting + ", " + name)

def sum (x,b): # variable
    return x+b

def explain(*content): # multiple arguments (args)
    print("Length : " + str(len(content)))
    print("First : " + str(content[0])) ## read more at arrays
    print("Last : " + str(content[-1])) ## read more at arrays
    print("Content : ", end="")
    for x in content: ## read more at for loop
        print(x, end=" ")

def name(**name): # multiple arguments with keywords (kwargs)
    print("Last name : " + name["last"])
    print("First name : " + name["first"])
    print(name["last"] + ", " + name["first"])


#
# Test all
#

hello()
greet("Aki")
greet("Aki", "Alona!")
print(sum(69,31))
explain("Shirakami", "Ookami", "Nekomata", "Inugami")
name(first="Matsuri", last="Natsuiro")