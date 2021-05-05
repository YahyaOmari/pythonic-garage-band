from abc import ABC, abstractmethod
# class Band:
#     def __init__(self, name, play_solos):
class Guitarist:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"My name is {Guitarist1.name} and I play guitar")

Guitarist1 = Guitarist("Joan Jett")
Guitarist1.show_name()


class Drummer:
    def __init__(self, drummer):
        self.drummer = drummer

    def show_drummer(self):
        print(f"My name is {Drummer1.drummer} and I play drums")


Drummer1 = Drummer("Sheila E.")
Drummer1.show_drummer()
# class Bassist:

# class Musician:


# class Band:
#     def __init__ (self, name, members):
#         self.name=name
#         self.members=super
        

