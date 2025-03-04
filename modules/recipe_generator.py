import random

class RecipeGenerator:
    def __init__(self):
        self.recipes = {
    "rice": ["Fried Rice", "Biryani", "Rice Bowl", "Khichdi", "Pulao", "Lemon Rice", "Jeera Rice"],
    "eggs": ["Omelet", "Boiled Eggs", "Egg Curry", "Egg Bhurji", "Scrambled Eggs", "Egg Fried Rice"],
    "milk": ["Pancakes", "Milkshake", "Kheer", "Custard", "Hot Chocolate", "Rabri", "Milk Pudding"],
    "bread": ["Sandwich", "Bread Toast", "Garlic Bread", "Bread Pakora", "French Toast"],
    "chicken": ["Butter Chicken", "Chicken Curry", "Chicken Tikka", "Chicken Biryani", "Grilled Chicken"],
    "mutton": ["Mutton Curry", "Rogan Josh", "Keema", "Mutton Korma", "Mutton Biryani"],
    "fish": ["Grilled Fish", "Fish Curry", "Fish Tikka", "Fish Fry", "Fish Soup"],
    "potatoes": ["Aloo Paratha", "Mashed Potatoes", "French Fries", "Aloo Tikki", "Potato Wedges"],
    "onions": ["Onion Rings", "Caramelized Onions", "Onion Soup", "Onion Pakora", "Stuffed Onions"],
    "tomatoes": ["Tomato Soup", "Tomato Chutney", "Tomato Pasta", "Tomato Salad", "Stuffed Tomatoes"],
    "carrots": ["Carrot Halwa", "Carrot Soup", "Carrot Cake", "Carrot Salad", "Carrot Juice"],
    "spinach": ["Palak Paneer", "Spinach Soup", "Spinach Paratha", "Spinach Salad", "Creamed Spinach"],
    "cheese": ["Cheese Pizza", "Cheese Sandwich", "Cheese Omelet", "Cheese Pasta", "Cheese Sticks"],
    "butter": ["Butter Naan", "Butter Chicken", "Garlic Butter Pasta", "Butter Rice", "Butter Pancakes"],
    "yogurt": ["Raita", "Yogurt Parfait", "Lassi", "Greek Yogurt", "Yogurt Smoothie"],
    "peanuts": ["Peanut Butter", "Peanut Chutney", "Peanut Salad", "Roasted Peanuts", "Peanut Brittle"],
    "almonds": ["Almond Milk", "Almond Cake", "Badam Halwa", "Roasted Almonds", "Almond Cookies"],
    "cashews": ["Cashew Curry", "Cashew Barfi", "Cashew Butter", "Cashew Rice", "Cashew Milkshake"],
    "walnuts": ["Walnut Brownies", "Walnut Salad", "Walnut Cookies", "Walnut Halwa", "Walnut Milkshake"],
    "flour": ["Chapati", "Roti", "Puri", "Naan", "Paratha"],
    "cornflakes": ["Cornflakes Chaat", "Cornflakes Pudding", "Cornflakes Smoothie", "Cornflakes Bars", "Cornflakes Cookies"],
    "honey": ["Honey Glazed Chicken", "Honey Cake", "Honey Pancakes", "Honey Lemon Tea", "Honey Roasted Nuts"],
    "jam": ["Jam Sandwich", "Jam Tarts", "Jam Cookies", "Jam Roti", "Jam Milkshake"],
    "olive oil": ["Olive Oil Pasta", "Olive Oil Salad Dressing", "Olive Oil Bread", "Olive Oil Roasted Vegetables", "Olive Oil Marinade"],
    "soy sauce": ["Soy Sauce Noodles", "Soy Sauce Fried Rice", "Soy Sauce Chicken", "Soy Sauce Stir Fry", "Soy Sauce Marinade"],
    "vinegar": ["Vinegar Pickles", "Vinegar Salad Dressing", "Vinegar Sauce", "Vinegar Chips", "Vinegar Marinade"],
    "pasta": ["White Sauce Pasta", "Red Sauce Pasta", "Pesto Pasta", "Mac and Cheese", "Baked Pasta"],
    "lentils": ["Dal Tadka", "Dal Makhani", "Masoor Dal", "Lentil Soup", "Dal Chawal"],
    "chickpeas": ["Chole", "Hummus", "Chickpea Salad", "Chana Masala", "Chickpea Soup"],
    "black beans": ["Black Bean Soup", "Black Bean Salad", "Black Bean Tacos", "Black Bean Rice", "Black Bean Stir Fry"],
    "green peas": ["Matar Paneer", "Green Peas Pulao", "Green Peas Soup", "Aloo Matar", "Peas Paratha"],
    "raisins": ["Raisin Cookies", "Raisin Cake", "Raisin Halwa", "Raisin Salad", "Raisin Bars"],
    "coconut": ["Coconut Barfi", "Coconut Ladoo", "Coconut Chutney", "Coconut Curry", "Coconut Rice"],
    "apples": ["Apple Pie", "Apple Juice", "Apple Salad", "Baked Apples", "Apple Smoothie"],
    "bananas": ["Banana Smoothie", "Banana Pancakes", "Banana Chips", "Banana Ice Cream", "Banana Bread"],
    "oranges": ["Orange Juice", "Orange Cake", "Orange Salad", "Orange Marmalade", "Orange Smoothie"],
    "grapes": ["Grape Juice", "Grape Salad", "Grape Chutney", "Grape Smoothie", "Grape Tart"],
    "mangoes": ["Mango Shake", "Mango Ice Cream", "Mango Lassi", "Mango Chutney", "Mango Salad"],
    "strawberries": ["Strawberry Cake", "Strawberry Jam", "Strawberry Smoothie", "Strawberry Tart", "Strawberry Salad"],
    "pineapple": ["Pineapple Juice", "Pineapple Salad", "Pineapple Upside Down Cake", "Pineapple Smoothie", "Grilled Pineapple"],
    "zucchini": ["Zucchini Bread", "Zucchini Fritters", "Stuffed Zucchini", "Zucchini Soup", "Zucchini Salad"],
    "mushrooms": ["Mushroom Soup", "Mushroom Curry", "Stuffed Mushrooms", "Mushroom Pasta", "Grilled Mushrooms"],
    "garlic": ["Garlic Bread", "Garlic Butter Rice", "Garlic Noodles", "Garlic Soup", "Garlic Chicken"],
    "ginger": ["Ginger Tea", "Ginger Cookies", "Ginger Chicken", "Ginger Soup", "Ginger Chutney"],
    "beetroot": ["Beetroot Salad", "Beetroot Juice", "Beetroot Soup", "Beetroot Paratha", "Beetroot Halwa"],
    "cinnamon": ["Cinnamon Rolls", "Cinnamon Tea", "Cinnamon Cookies", "Cinnamon Cake", "Cinnamon Oatmeal"],
    "black pepper": ["Black Pepper Chicken", "Black Pepper Soup", "Black Pepper Noodles", "Black Pepper Salad", "Black Pepper Gravy"],
    "cardamom": ["Cardamom Tea", "Cardamom Cake", "Cardamom Cookies", "Cardamom Halwa", "Cardamom Lassi"],
    "turmeric": ["Turmeric Milk", "Turmeric Rice", "Turmeric Tea", "Turmeric Soup", "Turmeric Smoothie"],
    "cloves": ["Clove Tea", "Clove Soup", "Clove Chicken", "Clove Rice", "Clove Cookies"],
    "nutmeg": ["Nutmeg Cake", "Nutmeg Tea", "Nutmeg Cookies", "Nutmeg Halwa", "Nutmeg Ice Cream"]
}


    def generate_recipe(self, ingredients):
        available_recipes = [random.choice(self.recipes[item]) for item in ingredients if item in self.recipes]
        return available_recipes if available_recipes else ["No recipes found"]

if __name__ == "__main__":
    rg = RecipeGenerator()
    print(rg.generate_recipe(["rice", "eggs"]))
