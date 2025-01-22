# app/routes/fakestore.py
from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

FAKE_STORE_API_PRODUCTS = "https://fakestoreapi.com/products"
FAKE_STORE_API_CARTS = "https://fakestoreapi.com/carts"

@router.get("/products")
def get_products():
    """List all products from the Fake Store API."""
    response = requests.get(FAKE_STORE_API_PRODUCTS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch products.")
    return response.json()

@router.get("/products/{product_id}")
def get_product(product_id: int):
    """Get details of a single product by ID."""
    response = requests.get(f"{FAKE_STORE_API_PRODUCTS}/{product_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch product.")
    return response.json()

@router.post("/cart")
def add_to_cart(user_id: int, product_id: int, quantity: int):
    """Add an item to the user's cart."""
    payload = {
        "userId": user_id,
        "products": [
            {"productId": product_id, "quantity": quantity}
        ]
    }
    response = requests.post(FAKE_STORE_API_CARTS, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to add item to cart.")
    return response.json()

@router.get("/cart/{user_id}")
def get_cart(user_id: int):
    """List all items in a user's cart."""
    response = requests.get(f"{FAKE_STORE_API_CARTS}/user/{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch cart items.")
    return response.json()

@router.put("/cart/{cart_id}")
def update_cart(cart_id: int, products: list):
    """Update the contents of a cart by ID."""
    payload = {
        "products": products
    }
    response = requests.put(f"{FAKE_STORE_API_CARTS}/{cart_id}", json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to update cart.")
    return response.json()

@router.delete("/cart/{cart_id}")
def delete_cart(cart_id: int):
    """Delete a cart by ID."""
    response = requests.delete(f"{FAKE_STORE_API_CARTS}/{cart_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to delete cart.")
    return {"message": "Cart deleted successfully."}
