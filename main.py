# FUNCTIONAL

def flat_sort(array):
    new_array = []
    for item in array:
            new_array.append(item)
    return sorted(new_array)


'''
This method ensures data immutability as it returns a new list.

This is a pure function as it does not change the original data and it will always
return the same result for the same input.

This is not a higher-order function as it does not accept a function as an argument.

To my best knowledge, using this functional approach is a lot more straight forward for
something this simple.

'''

# OOP

class Podracer:
    def __init__(self, max_speed, condition, price):
         self.max_speed = max_speed
         self.condition = condition
         self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *=2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flames_jet(self, other):
        other.condition = "trashed"

'''

This solution demonstrates encapsulation, as it bundles the data and methods together,
inheritance, as the subclasses AnakinsPod and SebulbasPod inherit from the Podracer class,
and polymorphism, with the addition of the repair, boost and flames_jet methods.

I think using the OOP approach is the way to go for this solution as there can be multiple
aspects that can be changed in the future.

Solving this problem with OOP is more complex than using functional programming but with the inheritance
to the subclasses allowing code to be reused, and the flexibility to add methods accordingly, keeps
all code organized and maintainable. 

'''