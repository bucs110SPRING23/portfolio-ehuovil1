def star_pyramid(rows):
    for i in range(1, rows + 1):
        print("*" * i)


#define a function
def rstar_pyramid(stars):
    for i in range(stars, 0, -1):
        print("*" * i)

def rstar_pyramid():
    for i in range(levels, 0, -1):





levels = int(input("Enter the desired pyramid height: "))

star_pyramid(levels)
rstar_pyramid(levels)

def foo(x, y, z):
    print(x, y, z)

foo(1, 2, 3)
foo(2, 1, 3)