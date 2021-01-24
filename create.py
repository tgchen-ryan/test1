import requests
import json

apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjk3MDE2MzI2LCJ1aWQiOjE4MjMwOTc1LCJpYWQiOiIyMDIxLTAxLTI0VDA3OjI4OjIzLjIxM1oiLCJwZXIiOiJtZTp3cml0ZSIsImFjdGlkIjo3OTY5NTk4LCJyZ24iOiJ1c2UxIn0.SbQm1OhmO1P3T11FUdvqzvVKe6PMqGkrQC5NrhrPUMo'
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { create_item (board_id:980571385, item_name:$myItemName, column_values:$columnVals) { id } }'
vars = {
 'myItemName' : 'Create Item-1 By Ryan',
 'columnVals' : json.dumps({
   'status' : {'label' : 'Done'},
    'Priority': {'label' : ' Best effort'},
   'date4' : {'date' : '2021-01-24'}
 })
}

data = {'query' : query5, 'variables' : vars}
r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())