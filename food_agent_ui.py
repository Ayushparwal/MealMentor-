import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"  # Make sure your FastAPI backend is running

st.set_page_config(page_title="AI Food Agent", page_icon="🍽️", layout="wide")

st.title("🍽️ AI-Powered Food Agent")

# Tabs for different functionalities
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📅 Meal Plan", "🛒 Grocery Tracker", "🍳 Recipe Generator", "🛍️ Food Ordering", "📊 Nutrition Info"])

# Meal Planner
with tab1:
    st.subheader("📅 AI Meal Plan Generator")
    if st.button("Generate Meal Plan"):
        response = requests.get(f"{API_BASE_URL}/meal_plan")
        if response.status_code == 200:
            meal_plan = response.json()
            st.write("### 🥣 Breakfast:", meal_plan["breakfast"])
            st.write("### 🍛 Lunch:", meal_plan["lunch"])
            st.write("### 🍫 Snacks:", meal_plan["snacks"])
            st.write("### 🍽️ Dinner:", meal_plan["dinner"])
        else:
            st.error("Failed to fetch meal plan.")

# Grocery Tracker
with tab2:
    st.subheader("🛒 Smart Grocery Tracker")
    if st.button("Check Inventory"):
        response = requests.get(f"{API_BASE_URL}/inventory")
        if response.status_code == 200:
            inventory = response.json()
            st.json(inventory)
        else:
            st.error("Failed to fetch inventory.")

    item = st.text_input("Item to Update:")
    quantity = st.number_input("New Quantity:", min_value=0, step=1)

    if st.button("Update Inventory"):
        response = requests.post(f"{API_BASE_URL}/update_inventory/{item}/{quantity}")
        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Failed to update inventory.")

# Recipe Generator
with tab3:
    st.subheader("🍳 AI Recipe Generator")
    ingredients = st.text_input("Enter available ingredients (comma-separated):")
    if st.button("Generate Recipe"):
        response = requests.get(f"{API_BASE_URL}/recipe/{ingredients}")
        if response.status_code == 200:
            recipes = response.json()
            st.write("### Suggested Recipes:")
            for recipe in recipes:
                st.write(f"✅ {recipe}")
        else:
            st.error("Failed to fetch recipes.")

# Food Ordering
with tab4:
    st.subheader("🛍️ Auto Food Ordering")
    food_item = st.text_input("Enter food item to order:")
    if st.button("Order Food"):
        response = requests.post(f"{API_BASE_URL}/order_food/{food_item}")
        if response.status_code == 200:
            st.success(f"✅ {food_item} ordered successfully!")
        else:
            st.error("Failed to order food.")

# Nutrition Information
with tab5:
    st.subheader("📊 Nutrition & Cost Analysis")
    food_item = st.text_input("Enter food item to check:")
    if st.button("Get Nutrition Info"):
        response = requests.get(f"{API_BASE_URL}/nutrition/{food_item}")
        if response.status_code == 200:
            nutrition = response.json()
            st.write(f"### 🍽️ {food_item}")
            st.write(f"Calories: {nutrition['calories']} kcal")
            st.write(f"Estimated Cost: ₹{nutrition['cost']}")
        else:
            st.error("Failed to fetch nutrition info.")
