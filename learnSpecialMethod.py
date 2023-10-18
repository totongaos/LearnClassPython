# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1)
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}\n({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)

def printPetNames(owner, **pets):
  print(f"Owner Name: {owner}")
  for pet, name in pets.items():
    print(f"{pet}: {name}")


printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
"""
Owner Name: Jonathan
dog: Brock
fish: ['Larry', 'Curly', 'Moe']
turtle: Shelldon
"""