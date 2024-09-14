from dotenv import load_dotenv
import os
import streamlit as st
# from pymongo import MongoClient
from pprint import pprint 
import json
#--IMPORT PATHS----------

load_dotenv()
IMAGES=os.getenv("IMAGES")
LOGO_IMAGE=os.getenv("LOGO_IMAGE")


# Define the path for user data
USER_DATA_PATH = 'userdetails/users.json'

# Ensure the userdetails directory exists
os.makedirs('userdetails', exist_ok=True)

# Load user data from JSON file
def load_users():
    if os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, 'r') as file:
            return json.load(file)
    return {}



# Save user data to JSON file
def save_users(users):
    with open(USER_DATA_PATH, 'w') as file:
        json.dump(users, file, indent=4)

# Create a new user
def create_user(username, password, role):
    users = load_users()
    if username in users:
        return False  # User already exists
    users[username] = {'password': password, 'role': role}
    save_users(users)
    os.makedirs(f"UserWorkspace/{username}")
    return True

# Delete an existing user
def delete_user(username):
    users = load_users()
    if username in users:
        del users[username]
        save_users(users)
        return True
    return False

# Edit an existing user
def edit_user(username, new_password, new_role):
    users = load_users()
    if username in users:
        # Update password and role, but do not need to mention current password
        users[username] = {'password': new_password, 'role': new_role}
        save_users(users)
        return True
    return False

# Check credentials
def check_credentials(username, password):
    users = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]['role']
    return None


    