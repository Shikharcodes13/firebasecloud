import requests
from app.models import CartItem

FAKE_STORE_API_URL = "https://fakestoreapi.com/products"

cart = []  # In-memory cart to simulate a simple shopping cart

async def get_all_products():
    response = requests.get(FAKE_STORE_API_URL)
    if response.status_code == 200:
        return response.json()  # Returns all products from the Fake Store API
    return {"error": "Failed to fetch products from Fake Store"}

async def add_item_to_cart(item: CartItem):
    cart.append(item)
    return {"message": f"Item '{item.title}' added to the cart."}

async def get_cart_items():
    return {"cart": cart}
