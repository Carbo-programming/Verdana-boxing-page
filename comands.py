from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
    #return 'Hola'
    dato = {
        'titulo' : 'hola',
        'bievenida':'saludos',
        'lista' : ['buenas','hola','buena tarde','saludos']
    }
    return render_template('index.html',data=dato)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre,edad):
    data={
        'titulo' : 'cotacto',
        'nombre' : nombre,
        'edad' : edad
    }
    return render_template('contacto.html',data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('p1'))
    print(request.args.get('p2'))
    return 'a'

def pagina_no_encontrada(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__ =='__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True) 