#loop methode
# Nia Bi

def factorielle(n):
    if n == 0:
        return 1
    else:
        F=1
        for i in range(1,n+1):
            F=F*i
        return F
    
if __name__ == '__main__': 
    print("factorielle calculator")
    n = int(input("Enter a number: "))
    print(f"The factorial of {n} is {factorielle(n)}")