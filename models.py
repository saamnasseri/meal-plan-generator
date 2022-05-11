class Meal():
    def __init__(self, name, calories, protein, fat, carbs, price, restrictions, type, ethnicity):
        self.name = name
        self.protein = protein
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.restricitons = restrictions
        self.price = price
        self.type = type
        self.ethnicity = ethnicity
   
    def __repr__(self) -> str:
        rep = self.name + ' ' + str(self.calories) + ' cals, ' + str(self.protein) + ' grams protein, ' + str(self.price) + '$'
        return rep


