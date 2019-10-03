import json
import requests
from requests import Response
val=[]
response=requests.post('http://localhost:8000/notes/',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({"title": "abc111",
                               "description": "YYYYYYY",
                               "created_at": "AP",
                               "created_by": "abc",
                               "priority": 1,
                               "books": [
                                   {
                                        "name": "YYY"
                                   }
                               ]
                               }))
val.append(response)
print(val)

# cat post.json | http POST http://localhost:8000/notes
valput=[]
abc=requests.put('http://localhost:8000/notes/1',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({"title": "abc123",
                               "description": "xxxxxxxxx",
                               "created_at": "TN",
                               "created_by": "def",
                               "priority": 1,
                               "books": [
                                   {
                                        "name": "xyz"
                                   }
                               ]
                               }))
valput.append(abc)
print(valput)
