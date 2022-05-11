from calendar import c
from flask import Blueprint, render_template, request
from models import Meal
import random

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')


@auth.route('/', methods=['GET', 'POST'])
def login():
    return render_template("index.html")

@auth.route('/save', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    meals = []

    """ Breakfast """
    meals.append(Meal("Omlette", 500, 27, 14, 60, 14, "Vegan", ["Breakfast"], None))
    meals.append(Meal("Lentils", 280, 32, 0, 130, 5, None, ["Breakfast", "Lunch"], None))
    meals.append(Meal("Oatmeal", 520, 10, 7, 115, 8, "Vegan", ["Breakfast"], None))
    meals.append(Meal("French Toast", 400, 24, 18, 80, 7, "Vegan", ["Breakfast"], None))
    meals.append(Meal("Breakfast burrito", 636, 30, 33, 44, 12, None, ['Breakfast'], 'Mexican'))
    meals.append(Meal("Bacon and Eggs", 480, 26, 16, 28, 8, "Vegan", ["Breakfast"], None))
    meals.append(Meal("Chile", 250, 18, 20, 64, 6, "Vegan", ["Breakfast"], None))
    meals.append(Meal("Khaman Dhoka", 175, 8, 2, 30, 9, "Vegan",  ["Breakfast"], "Indian"))
    """ Lunch """
    meals.append(Meal("Tuna Sandwich", 500, 50, 24, 75, 7, "Vegan", ["Lunch", "Snack"], None))
    meals.append(Meal("Turkey Sandwich", 580, 33, 20, 80, 8, "Vegan", ["Lunch", "Snacks"], None))
    meals.append(Meal("Salad Chirazi",  120, 4, 7, 25, 6, None, ["Lunch"], "Iranian"))
    meals.append(Meal("Trout Fillet", 320, 34, 13, 30, 12, "Vegan", ["Lunch"], None))
    meals.append(Meal("Chicken salad sandwich", 380, 26, 14, 90, 8, None, ["Lunch"], None))
    meals.append(Meal("Chicken pot pie", 315, 24, 9, 34, 6, None, ["Lunch"], None))
    meals.append(Meal("Asian Quinoa salad", 285, 13, 9, 38, 6, "Vegan", ["Lunch"], 'Asian' ))
    """ Dinner """
    meals.append(Meal("New York Steak with Quinoa",730, 40, 14, 7, 14, "Keto", ["Dinner"], None))
    meals.append(Meal("Elk Burger", 1000, 46, 12, 220, 15, None, ["Dinner"], None))
    meals.append(Meal("Kabob and rice", 830, 32, 122, 67, 12, None, ["Dinner"], "Iranian"))
    meals.append(Meal("Sphaggethi and meatballs", 780, 24, 12, 275, 13, "Pescatarian", ["Dinner"], None ))
    meals.append(Meal("Lobster tail", 1180, 36, 13, 42, 25, "Vegan", ["Dinner"], None))
    meals.append(Meal("Turmeric Chicken and rice", 620, 32, 13, 130, 8, None, ["Dinner"], "Iranian"))
    meals.append(Meal("Salmon and cilantro rice", 800, 32, 12, 120, 22, None, ["Dinner"], None))
    meals.append(Meal("Glazed Tri-tip steak", 600, 38, 19, 4, 12, 'Keto', ['Dinner'], None))
    meals.append(Meal("Buddha bowl", 415, 23, 17, 48, 9, 'None', ['Dinner'], 'Indian'))
    meals.append(Meal("Chicken Stir Fry", 350, 26, 13, 29, 6, None, ["Dinner"], None))
    """ Fillers """
    meals.append(Meal("Yogurt and Granola", 100, 24, 8, 22, 7, "Vegan", ["Filler"], None))
    meals.append(Meal('Banana', 100, 5, 4, 12, 1, 'Vegan', ['Filler'], None))
    meals.append(Meal("Two hard boiled eggs", 150, 14, 88, 10, 4, None, ['Filler'], None))
    meals.append(Meal("Fruit smoothie", 175, 8, 10, 30, 4, 'Vegan', ['Filler'], None))
    meals.append(Meal("English muffin with cream cheese", 200, 14, 8, 26, 4, None, ['Filler'], None))
    meals.append(Meal("Peanut Butter Sandwich", 250, 24, 12, 35, 5, "Vegan", ["Lunch", "Breakfast"], None))
    meals.append(Meal("Protein bar", 250, 32, 40, 15, 3, None, ['Filler'], None))
   


    height = int(data.getlist('height').pop())
    goal = data.getlist('goal').pop()
    fitnessLevel = data.getlist('fitness level').pop()
    restrictions = data.getlist('restrictions').pop()
    age = int(data.getlist('age').pop())
    weight = int(data.getlist('weight').pop())
    sex = data.getlist('sex').pop()
    budget = data.getlist('budget').pop()
    days = int(data.getlist('days').pop())
    """ get calorie intake """
    if fitnessLevel == 'Sedentary':
        fitnessLevel = 1
    elif fitnessLevel == 'Some':
        fitnessLevel = 2
    elif fitnessLevel =='Average':
        fitnessLevel = 3
    elif fitnessLevel == 'Good':
        fitnessLevel = 4
    elif fitnessLevel == 'Extraordinary':
        fitnessLevel = 5 
    
    if fitnessLevel == 1:
        macroTotal = int(weight/.42)
        carbs = int(macroTotal * .35)
        fat = int(macroTotal * .23)
    elif fitnessLevel == 2:
        macroTotal = int(weight/.42)
        carbs = int(macroTotal * .35)
        fat = int(macroTotal * .23)
    elif fitnessLevel == 3:
        macroTotal = int((weight + 15)/.40)
        carbs = int(macroTotal * .3)
        fat = int(macroTotal * .22)
    elif fitnessLevel == 4:
        macroTotal = int(weight/.40)
        carbs = int(macroTotal * .38)
        fat = int(macroTotal * .22)
    elif fitnessLevel == 5:
        macroTotal = int(weight/.40)
        carbs = int(macroTotal * .38)
        fat = int(macroTotal * .22)

    fitnessMulltiplyer = fitnessLevel * 150
    
    if sex == "Male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age) + int(fitnessMulltiplyer)
    else:
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age) + int(fitnessMulltiplyer)
    
    if goal == "Build muscle":
        getCalorieIntake = bmr + 500
    else:
        getCalorieIntake = bmr - 300
    
    if budget == "$":
        rbudget = 40
    elif budget == "$$":
        rbudget = 50
    elif budget == "$$$":
        rbudget = 60

    def plan():
        food = []
        caloriess = 0
        protein = 0
        budgetCount = 0
        discard = []
        """ create list of possible breakfasts and select one at random and remove it from meals list. after while loop finishes, re-add meals."""
        breakfast = []
        break_cals = getCalorieIntake * .33
        lunch_cals = getCalorieIntake * .33
        dinner_cals = getCalorieIntake * .33
        difference = 0
        while caloriess < .3 * getCalorieIntake:
            for b in meals:
                if ("Breakfast" in b.type):
                    breakfast.append (b)
                    discard.append(b)
                    meals.remove(b)
            food.append(random.choice(breakfast))
            for f in food:
                
                if f in breakfast:
                    caloriess += f.calories
                    breakfast.remove(f)
        else:
            difference = caloriess - getCalorieIntake  * .3
            if difference > 200:
                for g in food:
                    for i in range(int(difference) - 30, int(difference) + 30):
                        if i == g.calories:
                            food.remove(g)
        caloriess  = .3 * getCalorieIntake
        """ lunch """
        lunch = []
        
        while caloriess < .6 * getCalorieIntake:
            for t in meals:
                if ("Lunch" in t.type):
                    lunch.append(t)
                    discard.append(t)
                    meals.remove(t)
        
            food.append(random.choice(lunch))
    
            for g in food:
                
                if g in lunch:
                    caloriess += g.calories
                    """ 
                    protein += g.protein
                    budgetCount += g.price """
                    lunch.remove(g)   
        else:
            difference = caloriess - getCalorieIntake * .4
            if difference > 200:
                for g in food:
                    for i in range(int(difference) - 30, int(difference) + 30):
                        if i == g.calories:
                            food.remove(g)
        
        caloriess =  .6  *  getCalorieIntake
        """ dinner """
        dinner = []
        
        while caloriess < getCalorieIntake *  .7:
            for q in meals:
                if ("Dinner" in q.type):
                    dinner.append(q)
                    discard.append(q)
                    meals.remove(q)
            food.append(random.choice(dinner))
            for x in food:
                
                if x in dinner:
                    caloriess += q.calories
                    """ 
                    protein += q.protein
                    budgetCount += q.price """
                    dinner.remove(x)
        else:
            difference = caloriess - getCalorieIntake
            if difference > 200:
                for g in food:
                    for i in range(int(difference) - 30, int(difference) + 30):
                        if i == g.calories:
                            food.remove(g)
        
        for items in discard:
            meals.append(items)
        
        return food
        
    
    days_in_week = {
    "Sunday" : plan(),
    "Monday" : plan(),
    "Tuesday" : plan(),
    "Wednesday": plan(),
    "Thursday" : plan(),
    "Friday" : plan(),
    "Saturday" : plan()
    }

    def week_long(var):
    
        values_ = days_in_week.items()
        new_list = list(values_)
        a_value = new_list[0:var]
        if var > 7:
            num  = var - 7
            new_val = new_list[0:num]
            a_value += new_val
        return a_value
    
    week_long(days)
    
    return render_template("home.html", food = plan(), getCalorieIntake = round(getCalorieIntake), days = days, a_value = week_long(days), weight = weight)