import json
import requests
from requests import Response


def send_data(url, data):
    response = requests.post(url, json=data)
    return response


# send_data('http://localhost:8000/users/',{'username':'xxx'})
# send_data('http://localhost:8000/cars/', {'model':'aaa'})

#
# send_data('http://localhost:8000/LinkCartoUser/', {
#     'Car': 9,
#     'User': [10,11]
# })

# send_data('http://localhost:8000/LinkUsertoCar/', {
#     'User': 7,
#     'Car': [8, 9]
# })
# send_data('http://localhost:8000/UnLinkUsertoCar/', {
#     'User': 4,
#     'Car': [3, 5]
# })

send_data('http://localhost:8000/UnLinkCartoUser/', {
    'Car': 9,
    'User': [10, 11]
})
