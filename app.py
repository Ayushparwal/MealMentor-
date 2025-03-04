from fastapi import FastAPI
from modules.meal_planner import MealPlanner
from modules.grocery_manager import GroceryManager
from modules.recipe_generator import RecipeGenerator
from modules.food_ordering import FoodOrdering
from modules.nutrition_analysis import NutritionAnalysis

app = FastAPI()

meal_planner = MealPlanner()
grocery_manager = GroceryManager()
recipe_generator = RecipeGenerator()
food_ordering = FoodOrdering()
nutrition_analysis = NutritionAnalysis()

@app.get("/")
def home():
    return {"message": "Welcome to the AI Food Agent API!"}

@app.get("/meal_plan")
def get_meal_plan():
    return meal_planner.generate_meal_plan()

@app.get("/inventory")
def get_inventory():
    return grocery_manager.get_inventory()

@app.post("/update_inventory/{item}/{quantity}")
def update_inventory(item: str, quantity: int):
    return grocery_manager.update_inventory(item, quantity)

@app.get("/recipe/{ingredients}")
def get_recipe(ingredients: str):
    ingredient_list = ingredients.split(",")
    return recipe_generator.generate_recipe(ingredient_list)

@app.post("/order_food/{food_item}")
def order_food(food_item: str):
    return food_ordering.order_food(food_item)

@app.get("/nutrition/{food_item}")
def get_nutrition(food_item: str):
    return nutrition_analysis.get_nutrition(food_item)
