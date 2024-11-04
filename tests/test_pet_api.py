# tests/test_pet_api.py

import pytest
from utils.api_client import create_pet, get_pet, delete_pet
from utils import config
from config import generate_random_pet_data

def test_create_pet_success():
    """Positive test: successfully create a new pet and verify its details."""
    # Generate random pet data
    pet_data = generate_random_pet_data()

    # Create the pet
    response = create_pet(pet_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["name"] == pet_data["name"]

    # Verify the pet was created
    pet_response = get_pet(pet_data["id"])
    assert pet_response.status_code == 200, f"Expected 200, got {pet_response.status_code}"
    assert pet_response.json()["name"] == pet_data["name"]
    assert pet_response.json()["status"] == pet_data["status"]

    # Clean up
    delete_pet(pet_data["id"])

def test_get_nonexistent_pet():
    """Negative test: try to retrieve a pet that doesn't exist."""
    non_existent_pet_id = 99999  # An arbitrary ID that likely doesn't exist

    # Attempt to get a non-existent pet
    response = get_pet(non_existent_pet_id)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    assert response.json()["message"] == "Pet not found"
