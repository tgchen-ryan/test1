import requests
import json

apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjk3MDE2MzI2LCJ1aWQiOjE4MjMwOTc1LCJpYWQiOiIyMDIxLTAxLTI0VDA3OjI4OjIzLjIxM1oiLCJwZXIiOiJtZTp3cml0ZSIsImFjdGlkIjo3OTY5NTk4LCJyZ24iOiJ1c2UxIn0.SbQm1OhmO1P3T11FUdvqzvVKe6PMqGkrQC5NrhrPUMo'
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

#query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { change_column_value (board_id:980571385, item_id: 980571390, column_id: “Status”, value: “{“label”:[“Done”]}”) { id } }'

query5 = 'mutation ($myItemName: String!, $columnVals: JSON!) { change_column_value (board_id:980571385, item_id: 980571390, column_id: Status})}'
vars = {
    'status' : {'label' : 'Done'},
    }


data = {'query' : query5, 'variables' : vars}
r = requests.post(url=apiUrl, json=data, headers=headers) # make request
print(r.json())