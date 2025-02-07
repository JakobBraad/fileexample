def greet():
    """
    simple function printing hello
    :return:
    """
    print("Hello!")
    return 0

def greet_improved(name):
    """
    more complex greet that takes a name as param
    :param name:
    :return:
    """
    print("Hello", name)

greet_improved("John")
greet_improved("Jane")

def custom_op(x, y):
    """

    :param x:
    :param y:
    :return:
    """

    result = 10*x + y
    return result
print (custom_op(5,9))
x = custom_op(5, 9 )
print(f"the result of custom_op is: {x}")
x = custom_op(y=9, x=5)
print(f"the result of the custom_op is: {x}")

def bond_intro(name):
    print("the name is:", name)

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(bond_name("Jakob", "Braad"))
bond_intro(bond_name("Jakob", "Braad"))
