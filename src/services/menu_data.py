import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.menu()
    
    def menu(self):
        with open(self.path, 'r') as file:
            reade = csv.reader(file)
            next(reade)
            read = list(reade)
        
        for line in read:
            dish = Dish(line[0], float(line[1]))
            ingred = Ingredient(line[2])
            amount = int(line[3])

            if dish in self.dishes:
                for d in self.dishes:
                    if d == dish:
                        d.add_ingredient_dependency(ingred, amount)
            else:
                dish.add_ingredient_dependency(ingred, amount)
                self.dishes.add(dish)
