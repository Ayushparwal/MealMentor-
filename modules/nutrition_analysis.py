class NutritionAnalysis:
    def __init__(self):
        self.food_data = {
    "Oats": {"calories": 150, "cost": 30},
    "Paneer": {"calories": 300, "cost": 80},
    "Eggs": {"calories": 70, "cost": 10},
    "Rice": {"calories": 200, "cost": 20},
    "Bread": {"calories": 80, "cost": 25},
    "Butter": {"calories": 100, "cost": 40},
    "Cheese": {"calories": 250, "cost": 50},
    "Chicken": {"calories": 230, "cost": 120},
    "Mutton": {"calories": 250, "cost": 200},
    "Fish": {"calories": 180, "cost": 150},
    "Milk": {"calories": 120, "cost": 50},
    "Curd": {"calories": 60, "cost": 30},
    "Yogurt": {"calories": 100, "cost": 35},
    "Peanuts": {"calories": 300, "cost": 60},
    "Almonds": {"calories": 350, "cost": 100},
    "Cashews": {"calories": 400, "cost": 120},
    "Walnuts": {"calories": 350, "cost": 140},
    "Flour": {"calories": 350, "cost": 25},
    "Cornflakes": {"calories": 110, "cost": 40},
    "Chia Seeds": {"calories": 500, "cost": 80},
    "Sunflower Seeds": {"calories": 450, "cost": 70},
    "Pumpkin Seeds": {"calories": 450, "cost": 75},
    "Honey": {"calories": 300, "cost": 90},
    "Jam": {"calories": 250, "cost": 60},
    "Maple Syrup": {"calories": 270, "cost": 150},
    "Olive Oil": {"calories": 900, "cost": 250},
    "Soy Sauce": {"calories": 50, "cost": 40},
    "Vinegar": {"calories": 10, "cost": 30},
    "Ketchup": {"calories": 100, "cost": 35},
    "Mayonnaise": {"calories": 680, "cost": 90},
    "Mustard": {"calories": 60, "cost": 40},
    "Pickles": {"calories": 40, "cost": 30},
    "Coconut": {"calories": 350, "cost": 50},
    "Apples": {"calories": 50, "cost": 20},
    "Bananas": {"calories": 100, "cost": 10},
    "Oranges": {"calories": 45, "cost": 15},
    "Grapes": {"calories": 70, "cost": 40},
    "Mangoes": {"calories": 150, "cost": 50},
    "Strawberries": {"calories": 35, "cost": 60},
    "Blueberries": {"calories": 45, "cost": 80},
    "Pineapple": {"calories": 50, "cost": 55},
    "Avocado": {"calories": 160, "cost": 70},
    "Tomatoes": {"calories": 20, "cost": 30},
    "Onions": {"calories": 40, "cost": 20},
    "Potatoes": {"calories": 150, "cost": 25},
    "Carrots": {"calories": 40, "cost": 20},
    "Spinach": {"calories": 25, "cost": 15},
    "Broccoli": {"calories": 50, "cost": 35},
    "Cauliflower": {"calories": 55, "cost": 30},
    "Capsicum": {"calories": 30, "cost": 25},
    "Cucumber": {"calories": 15, "cost": 20},
    "Pumpkin": {"calories": 45, "cost": 30},
    "Radish": {"calories": 20, "cost": 15},
    "Beetroot": {"calories": 45, "cost": 25},
    "Zucchini": {"calories": 35, "cost": 40},
    "Mushrooms": {"calories": 25, "cost": 50},
    "Garlic": {"calories": 150, "cost": 40},
    "Ginger": {"calories": 80, "cost": 30}
}


    def get_nutrition(self, food_item):
        food_item = food_item.strip().title()  # Convert input to match stored keys
        return self.food_data.get(food_item, {"calories": "Unknown", "cost": "Unknown"})

if __name__ == "__main__":
    na = NutritionAnalysis()
    print(na.get_nutrition(" Paneer "))  # ✅ Should return {'calories': 300, 'cost': 80}
    print(na.get_nutrition("Eggs"))      # ✅ Should return {'calories': 70, 'cost': 10}
    print(na.get_nutrition("tofu"))      # ✅ Should return {'calories': 'Unknown', 'cost': 'Unknown'}