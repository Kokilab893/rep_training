# import json
import requests


# from requests import Response


def send_data(url, data):
    response = requests.post(url, json=data)
    return response


# send_data('http://localhost:8000/users/',{'username':'xxx'})
# send_data('http://localhost:8000/cars/', {'model':'aaa'})

resp = []
response = send_data('http://localhost:8000/LinkUsertoCar/', {
    'User': 4,
    'Car': [10,11]
})
resp.append(response)
print(resp)

# resp=[]
# response=send_data('http://localhost:8000/LinkCartoUser/', {
#     'Car': 13,
#    'User': [10, 11]
# })
# resp.append(response)
# print(resp)

# resp=[]
# response=send_data('http://localhost:8000/UnLinkUsertoCar/', {
#     'User': 8,
#     'Car': [2, 4]
# })
# resp.append(response)
# print(resp)

# resp = []
# response = send_data('http://localhost:8000/UnLinkCartoUser/', {
#     'Car': 10,
#     'User': [3, 2]
# })
# resp.append(response)
# print(resp)
