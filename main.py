from flask import Flask, render_template, redirect, url_for, request
from paquetes.lib_sql import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        consulta = request.form.get('libro')
        libros = buscar(consulta)
        print(libros)
        elegido = request.form.get('elegido')
        print (elegido)

        if libros == None and elegido == None:
            error = 'No tenemos este libro, pero gracias por confiar en nosotros... :)'
            context = {
                'error' : error
            }
            return render_template('index.html', **context)

        if elegido is not None:
            elegido = buscar(elegido)

            context = {
                'autor': elegido[0][0],
                'titulo': elegido[0][1],
                'precio': elegido[0][2],
                'año': elegido[0][3],
                'elegido': elegido
            }

        else:
            context = {
                'autor': libros[0][0],
                'titulo': libros[0][1],
                'precio': libros[0][2],
                'año': libros[0][3],
                'libros': libros
            }

        return render_template('index.html', **context)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)