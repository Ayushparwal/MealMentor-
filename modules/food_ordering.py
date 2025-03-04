import requests

class FoodOrdering:
    def __init__(self):
        self.api_url = "https://fake-food-api.com/order"  # Replace with actual API

    def order_food(self, food_item):
        response = requests.post(self.api_url, json={"item": food_item})
        return response.json() if response.status_code == 200 else {"error": "Failed to order"}

if __name__ == "__main__":
    fo = FoodOrdering()
    print(fo.order_food("Pizza"))
