class Duck:
    def speak(self):
        return "Quack"
 
class Robot:
    def speak(self):
        return "Beep"
 
def make_it_speak(thing):
    return thing.speak()


print(make_it_speak(Duck()))
print(make_it_speak(Robot()))

# 1.
# make_it_speack function will do work with both Duck and Robot
# because they have the same method name

# 2.
# Duck Typing: it dosn't matter what you are, but waht you can do
# like the code above, because bothd Duck and Robot have the same method
# it works although they are not children of shared parent
# Any way, it is better to work with Polymorphism
