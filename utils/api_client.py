# utils/api_client.py

import requests
from config import BASE_URL

def create_pet(pet_data):
    response = requests.post(BASE_URL, json=pet_data)
    return response

def get_pet(pet_id):
    response = requests.get(f"{BASE_URL}/{pet_id}")
    return response

def delete_pet(pet_id):
    response = requests.delete(f"{BASE_URL}/{pet_id}")
    return response
