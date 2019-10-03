import json
import requests
from requests import Response

def send_data(url, data):
    response = requests.post(url, json=data)
    return response

# send_data('http://localhost:8000/users/',{'username':'xxx'})
# send_data('http://localhost:8000/cars/', {'model':'aaa'})


# send_data('http://localhost:8000/LinkUsertoCar/', {
#     'User': 7,
#     'Car': [8, 9]
# })

# send_data('http://localhost:8000/LinkCartoUser/', {
#     'Car': 9,
#     'User': [1, 2]
# })

send_data('http://localhost:8000/UnLinkUsertoCar/', {
    'User': 8,
    'Car': [6, 9]
})

# send_data('http://localhost:8000/UnLinkCartoUser/', {
#     'Car': 9,
#     'User': [7, 11]
# })
