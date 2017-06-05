
class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):
    def __init__(self, name, chases_cats):
        self.chases_cats = chases_cats
        super().__init__(name, "Dog")
        #Pet.__init__(self, name, "Dog")

    def chases_cats(self):
        return self.chases_cats

    def get_name(self):
        return "OVERRIDDEN NAME"


class Cat(Pet):
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hates_dogs(self):
        return self.hates_dogs


dog1 = Dog("dog1", "chases cat")
dog2 = Dog("dog2", "chases cat as well")
print(dog1.get_name())
print(dog2.get_name())
print(dog1.__str__())


print(Pet.get_name(dog1))


p = Pet("Pet", "Pet")
print(isinstance(p, Pet))
print(isinstance(dog1, Pet))
print(isinstance(p, Dog))





