import random
#Part A
weeks = 16
print(weeks, type(weeks)) 
classes = 5
print(classes, type(classes)) 
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
classes_per_week = 2
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("The cost per class is $" + str(cost_per_class))
List = ("Hockey", "Soccer", "Basketball", "Tennis", "Football")
RandomChoice = random.choice(List)
print(RandomChoice)