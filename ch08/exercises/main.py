import turtle

print("hello")


class Num:
    
    def __init__(self, n) -> None:
        self.data = n
        self.x = "string"

class Foo:

   # def __init__(self, x, y, z, a, b, c) -> None:
   #     self.x = x
   #     self.y = y
   #     self..... #rest of parameters

   def __init__(self, **kwargs) -> None:
       self.__dict__ = kwargs


def __str__(self) -> None:
#double under
# no parameters other than 'self'
# must return a string



def main() -> None:

    mynum = Num(7)
    mynum2 = Num(9)
    mynum3 = {'data': 7, "x": "string"}

    print(mynum.data)
    print(mynum2.data)
   # print(mynum3['data'])
   # print(mynum.__dict__)

    mynum.addone() # calling method in class
    addone(mynum) # calling the function
    print(mynum.data)
    mynum2.addone()
    print
    dictionary = {'x': 1, 'y':, }

    t = turtle.Turtle()
    t.forward(56)

    mylist = []

    mystr = "HellO"
    
    length = len(mystr)
    mylist = [1,2,3]
    list_length = len()

    upper_str = mystr.upper()
    split_str = mystr.split("ll")

num = 5
print(f"The number is: {num")
mynewnum = Num(5)
print(f"The number is: {mynewnum}")







main()
