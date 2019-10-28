from flask import Flask, render_template, redirect, url_for, request
from paquetes.lib_sql import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        consulta = request.form.get('libro')
        libros = buscar(consulta)

        if libros == None:
            error = 'No tenemos este libro, pero gracias por confiar en nosotros... :)'
            context = {
                'error' : error
            }
            return render_template('index.html', **context)

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