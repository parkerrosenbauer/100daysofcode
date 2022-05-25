# Day 37 of 100 Days of Code Challenge
# Habit Tracker using the Pixela API
# view the tracker at: https://pixe.la/v1/users/parkerrosen/graphs/writinggraph.html

import requests
from datetime import datetime

USERNAME = "parkerrosen"
TOKEN = "1234567"  # dummy token
GRAPH_ID = "writinggraph"

today = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# create pixela account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create a pixela graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Words Written Graph",
    "unit": "word",
    "type": "int",
    "color": "ichou"  # yellow
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# update the pixela graph
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_config = {
    "unit": "words"
}
# response = requests.put(url=update_graph_endpoint, json=update_config, headers=headers)
# print(response.text)

# post a pixel to the graph
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today,
    "quantity": input("How many words did you type today?"),
}
response = requests.post(url=post_endpoint, json=pixel_config, headers=headers)
print(response.text)
