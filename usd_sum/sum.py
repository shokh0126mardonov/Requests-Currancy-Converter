def usd_to_sum():
    import requests
    from pprint import pprint
    import json

    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    responce = requests.get(url)
    content = responce.content.decode()
    data = json.loads(content)

    for i in data:
        if i['id'] == 69:
            id = i
            
    usd_to_sum = int(input("Dollar miqdorini kiriting: "))
    summa = float(id['Rate']) * usd_to_sum
    print(f"{summa:_.2f}")
    
