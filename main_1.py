import requests
import json
from monday.utils import monday_json_stringify

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDAzNjI2NCwidWlkIjozMDI4NTQ1NSwiaWFkIjoiMjAyMi0wNS0xMVQxNDo1NzoyNi4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIwNzg4NjYsInJnbiI6InVzZTEifQ.3cZrIGgvUzaUke3KG_WFuaCk3XZ9Lh7mVD3osed1Z4I"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}

def get_items_by_group_query(board_id, group_id):
    query = '''query
    {
        boards(ids: %s) {
            groups(ids: "%s") {
                id
                title
                items {
                id
                column_values{
                    text}
                }
            }
        }
    }''' % (board_id, group_id)
    return query

#def look_for_email_when_have_item_id():

def look_for_id_email(email):
    query = get_items_by_group_query(2665323559, 'topics')
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    print(r.json())
    for i in range(len(r.json()['data']['boards'][0]['groups'][0]['items'])):
       cur_email=(r.json()['data']['boards'][0]['groups'][0]['items'][i]['column_values'][0]['text'])
       if cur_email==email:
            print(r.json()['data']['boards'][0]['groups'][0]['items'][i]['id'])
look_for_id_email('bayan@gmail.com')
