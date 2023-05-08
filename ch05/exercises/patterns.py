rows = int(input("Number of Rows: "))

stars = int(input("Number of Stars: "))

def star_pyramid(rows):
    for i in range(1, rows + 1):
        print("*" * i)

#define a function
def rstar_pyramid(stars):
    for i in range(stars, 0, -1):
        print("*" * i)

print(star_pyramid(rows))
print(rstar_pyramid(stars))



