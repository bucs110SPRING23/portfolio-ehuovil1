

#num1 = int(input("Enter number "))

def multiplication():
    product=0
    for i in range (num1): 
        product = product+num1      
    print("The product is: " + str(product))

#print(multiplication())


def exponent(factor, exponent):
    factor = input("Factor: ")
    exponent = input("Exponent: ")
    product = 0
    for i in range (exponent):
        product = factor * factor
    print("The result is: ")

print(exponent())
