class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
        
    def add_animal(self, animal, count):
        self.animals[animal] = count
        
    def show_animals(self):
        print (self.name, "'s farm")
        for animal, count in self.animals.items():
            print(f"{animal} : {count}")
        print("E-I-E-I-0!")
        
# Creating a new farm object
my_farm = Farm("McDonald")

# Adding animals to the farm
my_farm.add_animal("cow", 5)
my_farm.add_animal("sheep", 2)
my_farm.add_animal("goat", 12)

# Showing the animals on the farm
my_farm.show_animals()