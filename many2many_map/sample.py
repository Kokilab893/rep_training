import json
import requests
from requests import Response


def send_data(url, data):
    response = requests.post(url, json=data)
    return response


# send_data('http://localhost:8000/users/',{'username':'xxx'})
# send_data('http://localhost:8000/cars/', {'model':'aaa'})
# send_data('http://localhost:8000/cars/', json.dumps({
#         "model": "modela"
# }))
#
# send_data('http://localhost:8000/LinkCartoUser/', {
#     'Car': 3,
#     'User': [3,4,5]
# })

send_data('http://localhost:8000/LinkUsertoCar/', {
    'User': 4,
    'Car': [3, 5]
})
