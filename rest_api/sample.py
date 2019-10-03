import json
import requests
from requests import Response

val: Response = requests.post('http://localhost:8000/notes/',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({'title': 'sample note five' , 'description': 'sample notes',
                                    'created_at': '2017-08-18 00:00:00', 'created_by': 'abc',
                                    'priority': 2}))
# response =requests.post("data").uploadto('postgresql+psycopg2://postgres:postgres@localhost/SampleDB')

print(val)


requests.put('http://localhost:8000/notes/2',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({'title': 'sample note five' , 'description': 'sample notes edited',
                                    'created_at': '2017-08-18 00:00:00', 'created_by': 'abc',
                                    'priority': 2}))
requests.delete('http://localhost:8000/notes/3')
requests.get('http://localhost:8000/notes/4')

