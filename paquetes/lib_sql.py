import pymysql


def buscar(libro):

    conexion = pymysql.connect(
        'localhost', 'root', 'root', 'libreria')

    cursor = conexion.cursor()

    cursor.execute(f'''
        SELECT  a.name, b.title, b.price, b.year
        FROM books AS b
        JOIN authors AS a
        ON a.author_id = b.author_id
        WHERE b.title LIKE "%{libro}%"
        LIMIT 5;
    ''')
    
    datos = cursor.fetchall()

    if datos == ():
        datos = None

    conexion.commit()
    conexion.close()
    print(datos[0])
    return datos