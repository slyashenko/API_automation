# config.py

import random
import string

BASE_URL = "https://petstore.swagger.io/v2/pet"

# Function to generate a random pet ID
def generate_random_pet_id():
    return random.randint(10000, 99999)

# Function to generate random pet data
def generate_random_pet_data():
    pet_id = generate_random_pet_id()
    pet_name = ''.join(random.choices(string.ascii_letters, k=8))
    return {
        "id": pet_id,
        "name": pet_name,
        "status": "available"
    }
