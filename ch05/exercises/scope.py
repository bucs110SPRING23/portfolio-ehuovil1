

#num1 = int(input("Enter number "))

def multiplication(num1):
    product=0
    for i in range (num1): 
        product = product + num1 
    print(product)     
print(multiplication(2))
#print(multiplication())



def exponent(factor, num2):
    product = 0
    for i in range (num2):
        product = factor * factor
    print(product)
print(exponent(3, 3))

def square(a):
    squared = a * a
    print(squared)
print(square(5))


