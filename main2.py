import requests
import json
from monday.utils import monday_json_stringify

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDAzNjI2NCwidWlkIjozMDI4NTQ1NSwiaWFkIjoiMjAyMi0wNS0xMVQxNDo1NzoyNi4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIwNzg4NjYsInJnbiI6InVzZTEifQ.3cZrIGgvUzaUke3KG_WFuaCk3XZ9Lh7mVD3osed1Z4I"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}




def get_column_value_Email_part(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids

    return query

query = get_column_value_Email_part(2665335591)
data = {'query': query}
r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
#print(r.json())
#print(r.json()['data']['items'][0]['column_values'][0]['text'])


#################################################################################################


def get_column_value_Email_tutur(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids

    return query

query1 = get_column_value_Email_tutur(2665335591)
data1 = {'query': query1}
r1 = requests.post(url=apiUrl, json=data1, headers=headers)  # make request
#print(r1.json())
#print(r1.json()['data']['items'][0]['column_values'][3]['text'])




###############################################################################################################


def get_column_value_coin(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids

    return query

query2 = get_column_value_coin(2667191012)
data2 = {'query': query2}
r2 = requests.post(url=apiUrl, json=data2, headers=headers)  # make request
#print(r2.json())
#print(r2.json()['data']['items'][0]['column_values'][1]['text'])
