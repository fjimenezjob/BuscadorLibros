from flask import Flask, render_template, redirect, url_for, request
from paquetes.lib_sql import buscar

app = Flask(__name__)

INIT_PAGE= 'index.html'


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        consulta = request.form.get('libro')
        libros = buscar(consulta)
        elegido = request.form.get('elegido')


        if libros == None and elegido == None:
            error = 'No tenemos este libro, pero gracias por confiar en nosotros... :)'
            context = {
                'error' : error
            }
            return render_template(INIT_PAGE, **context)

        if elegido is not None:
            elegido = buscar(elegido)

            context = {
                'autor': elegido[0][0].capitalize(),
                'titulo': elegido[0][1].capitalize(),
                'precio': elegido[0][2],
                'año': elegido[0][3],
                'elegido': elegido
            }

        else:
            context = {
                'autor': libros[0][0].capitalize(),
                'titulo': libros[0][1].capitalize(),
                'precio': libros[0][2],
                'año': libros[0][3],
                'libros': libros
            }

        return render_template(INIT_PAGE, **context)
    return render_template(INIT_PAGE)


if __name__ == "__main__":
    app.run(debug=True)