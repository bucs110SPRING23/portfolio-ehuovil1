import random
#Part A
weeks = 16
print(weeks, type(weeks)) #'var' is the variable name
classes = 5
print(classes, type(classes)) #'var' is the variable name
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
cost_per_class = cost_per_week / classes_per_week
print("The cost per class is $" + str(cost_per_class))