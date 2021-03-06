import requests
import json
from monday.utils import monday_json_stringify

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE2MDAzNjI2NCwidWlkIjozMDI4NTQ1NSwiaWFkIjoiMjAyMi0wNS0xMVQxNDo1NzoyNi4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTIwNzg4NjYsInJnbiI6InVzZTEifQ.3cZrIGgvUzaUke3KG_WFuaCk3XZ9Lh7mVD3osed1Z4I"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}



def help_get_column_value_Email_part(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids
    return query
def get_column_value_Email_part(ids):
    query = help_get_column_value_Email_part(ids)
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    return(r.json()['data']['items'][0]['column_values'][0]['text'])

def help_get_column_value_Email_tutur(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids

    return query

def get_column_value_Email_tutur(ids):
    query1 = help_get_column_value_Email_tutur(ids)
    data1 = {'query': query1}
    r1 = requests.post(url=apiUrl, json=data1, headers=headers)  # make request
    return (r1.json()['data']['items'][0]['column_values'][3]['text'])


def help_get_column_value_coin(ids):
    query = '''query
            {
                items (ids: %s) {
                    column_values {
                        text
                    }
                }
            }''' % ids

    return query

def get_column_value_coin(ids):
    query2 = help_get_column_value_coin(ids)
    data2 = {'query': query2}
    r2 = requests.post(url=apiUrl, json=data2, headers=headers)  # make request
    return(r2.json()['data']['items'][0]['column_values'][1]['text'])
    #print(r2.json())

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

def look_for_id_email(email):
    query = get_items_by_group_query(2665323559, 'topics')
    data = {'query': query}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    for i in range(len(r.json()['data']['boards'][0]['groups'][0]['items'])):
       cur_email=(r.json()['data']['boards'][0]['groups'][0]['items'][i]['column_values'][0]['text'])
       if cur_email==email:
            return (r.json()['data']['boards'][0]['groups'][0]['items'][i]['id'])

def get_items_by_group_query(board_id, group_id):
    query = '''query
    {
        boards(ids: %s) {
            groups(ids: "%s") {
                id
                title
                items {
                    id
                    name
                    column_values{
                    text
                    }  
                }
            }
        }
    }''' % (board_id, group_id)
    return query

def get_boards_query(**kwargs):
    query = '''query
    {
        boards (%s) {
            id
            name
            permissions
            tags {
              id
              name
            }
            groups {
                id
                title
            }
            columns {
                id
                title
                type
            }
        }
    }''' % ', '.join(["%s: %s" % (arg, kwargs.get(arg)) for arg in kwargs])
    return query


def help_delete_item_query(item_id):
    query = '''
    mutation
    {
        delete_item (item_id: %s)
        {
            id
        }
    }''' % (item_id)
    return query

def delete_item_query(item_id):
    query1 = help_delete_item_query(item_id)
    data1 = {'query': query1}
    r1 = requests.post(url=apiUrl, json=data1, headers=headers)
    r1.json()


def maya():
    query2 = get_boards_query()
    data2 = {'query': query2}
    r2 = requests.post(url=apiUrl, json=data2, headers=headers)  # make request
    #print(r2.json())
    for boards in r2.json()['data']['boards']:
        if (boards['id']!=2665323559):
            for group in boards['groups']:
                query3 = get_items_by_group_query(boards['id'], group['id'])
                data3 = {'query': query3}
                r3 = requests.post(url=apiUrl, json=data3, headers=headers)
                for item in r3.json()['data']['boards'][0]['groups'][0]['items']:
                    print(get_column_value_Email_part(item['id']))

                    #print(get_column_value_coin(look_for_id_email(get_column_value_Email_part(item['id']))))
                   # if (get_column_value_coin(get_column_value_Email_part(item['id'])) <= 0):
                         # delete_item_query(item['id'])
                   # print(get_column_value_coin(look_for_id_email(get_column_value_Email_part(item['id']))))
                    #print(item['column_values'][0][3])

maya()

