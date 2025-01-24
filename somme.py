# somme calculator
# Nia Bi

def addition(a, b):
    return a + b

if __name__ == '__main__':
    print("somme calculator")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"The sum of {a} and {b} is {addition(a, b)}")