import requests

def get_users():
    response = requests.get('http://127.0.0.1:5000/users')
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(user)
    else:
        print('Failed to retrieve users')

# Test the client
get_users()