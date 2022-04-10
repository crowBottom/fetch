import requests

def get_all_list_items():
    res = requests.get('https://fetch-hiring.s3.amazonaws.com/hiring.json')
    data = res.json()

    list = []
    for item in data:
        if item['name'] != "":
            list.append(item)
    return list
