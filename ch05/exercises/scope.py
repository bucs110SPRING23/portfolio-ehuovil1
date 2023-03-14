

#num1 = int(input("Enter number "))

def multiplication(num1, num3):
    product=0
    for i in range (num3): 
        product = product + num1 
    print(product)     
print(multiplication(2, 3))
#print(multiplication())



def exponent(factor, num2):
    product = 0
    for i in range (num2):
        product = product + factor * factor
    print(product)
print(exponent(3, 3))

def square(a):
    squared = a * a
    print(squared)
print(square(5))


