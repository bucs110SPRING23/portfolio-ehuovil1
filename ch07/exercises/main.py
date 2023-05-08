import turtle
import pygame
t = turtle.Turtle()
print(type(t))
print(type(1))

#class are blueprint for objects
# - functions are stored algorithms
# - class as a stored data type
# - classes are not executable
# - don't put executabpe 

#class Point:
    
# - snakecase: snake_case, underscores for spaces, all lowercase
# - camelcase: camelCase, capital for spaces, starts lowercase

points = []
for p in range (10):
    x = random.randint(0, 250)
    y = random.randint(0, 250)
    points.append(point.Point(x,y))






t = turtle.Turtle()
for p in points:
    p.random_color()
    t.color(p.color)
    t.goto(p.xcoor, p.ycoor)

turtle.Screen(). exitonclick()


pygame.init()
display = 
