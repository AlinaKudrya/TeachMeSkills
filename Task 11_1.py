class Tree:
    def __init__(self, height, tree_family, diameter):
        self.height = height
        self.tree_family = tree_family
        self.diameter = diameter

    def get_height(self):
        return self.height

    def set_height(self,height):
        self.height = height

    def get_tree_family(self):
        return self.tree_family

    def set_tree_family(self, tree_family):
        self.tree_family = tree_family

    def get_diameter(self):
        return self.diameter

    def set_diameter(self, diameter):
        self.diameter = diameter

    def do_fruits_grow(self):
       if self.tree_family == 'Coniferous':
           print('There are cones growing on these trees')
       elif self.tree_family == 'Fruit':
           print('There are different fruits growing on these trees')
       else:
           print("I don't know this trees")

    def tree_age(self):
        age = (self.diameter / 2) / 0.2
        print(f'The approximate age of this tree: {age}')

new_tree = Tree(50,'Fruit',20)
new_tree.do_fruits_grow()
new_tree.tree_age()

print('\n')
########################################

class Cocktail():
    def __init__(self, alcohol_ml, juice_ml, additions):
        self.alcohol_ml = alcohol_ml
        self.juice_ml = juice_ml
        self.additions = additions

    def get_alcohol_ml(self):
        return self.alcohol_ml

    def set_alcohol_ml(self,alcohol_ml):
        self.alcohol_ml = alcohol_ml

    def get_juice_ml(self):
        return self.juice_ml

    def set_juice_ml(self, juice_ml):
        self.juice_ml = juice_ml

    def get_additions(self):
        return self.additions

    def set_additions(self, additions):
        self.additions = additions

    def add_alcohol(self, amount):
        self.alcohol_ml += amount

    def add_juice(self,amount):
        self.juice_ml += amount

    def result(self):
        total_ml = self.alcohol_ml + self.juice_ml
        print(f'Your cocktail contains: alcohol: {round(self.alcohol_ml*100/total_ml)}%,'
              f' juice: {round(self.juice_ml*100/total_ml)}% and {self.additions}')

my_cocktail = Cocktail(100, 120, 'Orange')
my_cocktail.add_alcohol(50)
my_cocktail.add_juice(2)
my_cocktail.result()