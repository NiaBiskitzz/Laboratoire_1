# un programme qui calcule la factorielle d'un nombre
# Nia Bi

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)
    
if __name__ == '__main__':
    print("factorielle calculator")
    n = int(input("Enter a number: "))
    print(f"The factorial of {n} is {factorielle(n)}")