import random

class MealPlanner:
    def __init__(self):
        self.meals = {
    "breakfast": [
        "Oats with fruits", "Scrambled eggs", "Smoothie", "Poha", "Pancakes", "French toast", "Idli with sambar", "Upma",
        "Dosa with chutney", "Paratha with curd", "Muesli with yogurt", "Chia pudding", "Avocado toast", "Banana pancakes",
        "Boiled eggs", "Peanut butter toast", "Cornflakes with milk", "Waffles", "Breakfast burrito", "Egg sandwich",
        "Cheese omelette", "Methi thepla", "Sabudana khichdi", "Stuffed paratha", "Sprouts salad", "Tofu scramble",
        "Almond butter toast", "Vegetable uttapam", "Fruit smoothie bowl"
    ],
    "lunch": [
        "Grilled chicken salad", "Dal rice", "Paneer curry with roti", "Sushi", "Rajma chawal", "Chole bhature", "Biryani",
        "Butter chicken with naan", "Palak paneer", "Vegetable stir fry", "Chicken curry with rice", "Fish curry",
        "Veg pulao", "Lentil soup with bread", "Gobi paratha", "Pasta with garlic bread", "Mexican burrito bowl",
        "Tofu curry with quinoa", "Thai green curry", "Dhokla with chutney", "Mushroom risotto", "Kadhi pakora with rice",
        "Stuffed bell peppers", "BBQ chicken with roasted veggies", "Tandoori roti with dal makhani", "Shrimp fried rice",
        "Greek salad with pita bread", "Pav bhaji"
    ],
    "dinner": [
        "Grilled fish", "Vegetable soup", "Khichdi", "Pasta", "Chicken stir fry", "Roti with dal", "Vegetable biryani",
        "Miso soup with tofu", "Lemon garlic shrimp", "Stuffed capsicum", "Shakshuka", "Falafel with hummus",
        "Mushroom soup", "Chicken parmesan", "Vegetable curry with rice", "Soba noodles", "Tandoori chicken with salad",
        "Lauki sabzi with roti", "Vegetable fried rice", "Cabbage stir fry", "Egg fried rice", "Quinoa salad",
        "Thai basil chicken", "Stuffed zucchini boats", "Grilled eggplant with tahini", "Ratatouille", "Tomato basil pasta",
        "Baked salmon with asparagus", "Lentil stew with brown rice"
    ],
    "snacks": [
        "Nuts", "Fruit bowl", "Protein bar", "Chips", "Popcorn", "Hummus with veggie sticks", "Boiled chana", "Cheese cubes",
        "Dark chocolate", "Samosa", "Granola bar", "Greek yogurt with honey", "Masala peanuts", "Bhel puri", "Trail mix",
        "Rice cakes with peanut butter", "Roasted chickpeas", "Banana chips", "Stuffed dates", "Apple slices with almond butter",
        "Vegetable cutlets", "Smoothie bowl", "Corn on the cob", "Makhana", "Nachos with salsa", "Guacamole with tortilla chips",
        "Paneer tikka", "Mango lassi", "Chia seed pudding"
    ]
}


    def generate_meal_plan(self, dietary_preference=None):
        meal_plan = {
            "breakfast": random.choice(self.meals["breakfast"]),
            "lunch": random.choice(self.meals["lunch"]),
            "snacks": random.choice(self.meals["snacks"]),
            "dinner": random.choice(self.meals["dinner"])
        }
        return meal_plan

if __name__ == "__main__":
    planner = MealPlanner()
    print(planner.generate_meal_plan())
