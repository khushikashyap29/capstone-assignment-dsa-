# profiles.py

users = {}

def add_user(user_id, name, interests):
    users[user_id] = {
        "name": name,
        "interests": interests
    }

def get_profile(user_id):
    return users.get(user_id, "User not found")

def update_profile(user_id, name=None, interests=None):
    if user_id in users:
        if name:
            users[user_id]["name"] = name
        if interests:
            users[user_id]["interests"] = interests