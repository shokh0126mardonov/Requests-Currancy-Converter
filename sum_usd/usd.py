def sum_to_usd():   
    import requests
    import json
    from pprint import pprint

    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    responts = requests.get(url=url)
    content = responts.content.decode()
    data = json.loads(content)

    for i in data:
        if i['id'] == 69:
            money = float(i['Rate'])
            
    summa = float(input("Sum miqdorini kiriting : "))
    result = summa / money

    print(f"{result:.2f}")