import json

class GroceryManager:
    def __init__(self):
        self.inventory = {
            "Grains & Pulses": {
                "rice": 2, "flour": 2, "oats": 3, "lentils": 4, "chickpeas": 5, "black beans": 4, "green peas": 3
            },
            "Dairy & Eggs": {
                "milk": 1, "cheese": 1, "butter": 2, "yogurt": 2, "eggs": 6
            },
            "Vegetables": {
                "tomatoes": 3, "onions": 4, "potatoes": 6, "carrots": 3, "spinach": 3, "bell peppers": 4,
                "cabbage": 2, "cucumber": 3, "beetroot": 3, "broccoli": 2, "cauliflower": 3, "asparagus": 2,
                "zucchini": 2, "eggplant": 2, "radish": 3, "celery": 2
            },
            "Fruits": {
                "apples": 7, "bananas": 8, "oranges": 6, "lemons": 4, "grapes": 5, "strawberries": 6,
                "blueberries": 4, "avocado": 2, "pineapple": 1, "pears": 3, "watermelon": 1, "coconut": 2
            },
            "Meat & Seafood": {
                "chicken": 5, "fish": 3, "beef": 4, "canned tuna": 3
            },
            "Nuts & Seeds": {
                "peanuts": 5, "almonds": 4, "cashews": 3, "walnuts": 2, "sunflower seeds": 4, "chia seeds": 2
            },
            "Condiments & Spices": {
                "honey": 1, "olive oil": 2, "soy sauce": 1, "vinegar": 1, "cinnamon": 2, "turmeric": 2,
                "paprika": 2, "black pepper": 2, "cumin": 2, "cardamom": 1, "cloves": 1, "nutmeg": 1
            },
            "Bakery & Breakfast": {
                "bread": 2, "butter": 2, "jam": 2, "cereal": 4, "maple syrup": 1
            },
            "Beverages": {
                "coffee": 2, "tea": 3, "milk": 1
            },
            "Pasta & Noodles": {
                "pasta": 3, "noodles": 2
            }
        }

    def get_inventory(self):
        return self.inventory

    def suggest_groceries(self):
        suggestions = []
        for category, items in self.inventory.items():
            for item, qty in items.items():
                if qty < 2:
                    suggestions.append(item)
        return suggestions

    def update_inventory(self, item, quantity):
        for category in self.inventory:
            if item in self.inventory[category]:
                self.inventory[category][item] = quantity
                return f"{item} updated to {quantity}"
        return f"{item} not found in inventory."

if __name__ == "__main__":
    gm = GroceryManager()
    print(gm.suggest_groceries())
