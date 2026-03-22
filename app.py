from flask import Flask, render_template, redirect, url_for
import json
import os
import markdown

app=Flask(__name__)

def cargar_datos():
    with open('app/archivos/app.json','r', encoding='utf-8') as i:
        data = json.load(i)
    return data

#PAGINA PRINCIPAL
maxbox = 0
data = cargar_datos()
for i in data.values():
    if i['categoria'] == 'deportes':
        if maxbox < i['catnum']:
            maxbox = i['catnum']

data = cargar_datos()
#subcat entrenamiento
entre = [(key,i['catnum']) for key, i in data.items() if i['subcat'] == 'entrenamiento']
entrep = sorted(entre, key=lambda x: x[1], reverse=True)
#subcat tecnica
tec = [(key,i['catnum']) for key, i in data.items() if i['subcat'] == 'tecnica'] 
tecp = sorted(tec, key=lambda x: x[1], reverse=True)
#subcat comparativas
com = [(key,i['catnum']) for key, i in data.items() if i['subcat'] == 'comparativas'] 
comp = sorted(com, key=lambda x: x[1], reverse=True)
#subcat analisis
ana = [(key,i['catnum']) for key, i in data.items() if i['subcat'] == 'analisis'] 
anap = sorted(ana, key=lambda x: x[1], reverse=True)
#categoria boxeo
boxeo = [(key,i['numero']) for key, i in data.items() if i['categoria'] == 'boxeo']
boxeop = sorted(boxeo, key=lambda x: x[1], reverse=True)
@app.route('/')
def index():
    data = cargar_datos()
    max_item = max(data.values(), key=lambda x: x['numero'])
    nom=max_item['title']
    img=max_item['imagen']
    sub=max_item['subtexto']
    num=max_item['numero']
    cat=max_item['categoria']
    subc=max_item['subcat']
    print(max_item)
    return render_template('index.html',boxeop=boxeop,cat=cat,data=data,nom=nom,img=img,sub=sub,subc=subc,num=num,anap=anap,tecp=tecp,comp=comp,entrep=entrep)

#Pagina Deportes
data = cargar_datos()

#Pagina comun de informacion
data = cargar_datos()
def crear_vista(dato,contenido,html):
    def vista():
        return render_template(html,dato=dato,contenido=contenido)
    return vista

for i in data.keys():
    ruta_md = os.path.join('app','archivos','articulos',data[i]['text'])
    with open(ruta_md,'r',encoding='utf-8') as t:
        contenido_md = t.read()
    contenido = markdown.markdown(contenido_md)
    dato = data[i]
    app.add_url_rule(f'/{dato['categoria']}/{dato['subcat']}/{dato['title']}', dato['title'], crear_vista(dato,contenido,'base.html'))

#Pagina de subcategoria
lista_sub = [('boxeo','analisis',anap),('boxeo','entrenamiento',entrep),('boxeo','tecnica',tecp),('boxeo','comparativas',comp)]
for i in lista_sub:
    data = cargar_datos()
    sub = i[0]
    cat = i[1]
    app.add_url_rule(f'/{sub}/{cat}',f'{sub}_{cat}',crear_vista(data,i[2],'subcat.html'))

#Error 404
def pagina_no_encontrada(error):
    return redirect(url_for('index'))

#Correr la pagina
if __name__ =='__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True) 