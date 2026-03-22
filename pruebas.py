import json

def cargar_datos():
    with open('app/archivos/app.json','r', encoding='utf-8') as i:
        data = json.load(i)
    return data

data = cargar_datos()
boxeo = [(key,i['catnum']) for key, i in data.items() if i['categoria'] == 'boxeo']
boxeop = sorted(boxeo, key=lambda x: x[1], reverse=True)

print(boxeop)