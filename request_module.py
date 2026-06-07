# requests module
# The requests module is a popular third-party library used to send HTTP requests
# and communicate with web servers. It allows us to interact with web APIs,
# download data, upload data, and access online resources easily.

# In this example, we send a GET request to a web server to retrieve
# player information from an online API.

import requests

player_id = 101

# Send a GET request to the API endpoint
response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{player_id}"
)

# Check whether the request was successful
if response.status_code == 200:

    # Convert the JSON response into a Python dictionary
    player_data = response.json()

    # Display the player's information
    print("Player Name:", player_data["name"])
    print("Player Email:", player_data["email"])

else:
    print("Could not load player data.")
