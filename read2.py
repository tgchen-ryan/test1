import requests
import json

apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjk3MDE2MzI2LCJ1aWQiOjE4MjMwOTc1LCJpYWQiOiIyMDIxLTAxLTI0VDA3OjI4OjIzLjIxM1oiLCJwZXIiOiJtZTp3cml0ZSIsImFjdGlkIjo3OTY5NTk4LCJyZ24iOiJ1c2UxIn0.SbQm1OhmO1P3T11FUdvqzvVKe6PMqGkrQC5NrhrPUMo'
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query2 = '{boards(limit:1) { name id description items { name column_values{title id type text } } } }'
data = {'query' : query2}

r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())