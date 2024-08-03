import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(user='ramon', password='ramon', host='localhost', database='python_mysql', port='3306')
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM cliente')
        clientes = cursor.fetchall()
        print(clientes)  # Añade esta línea para verificar los datos
    connection.close()
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)

print(get_db_connection)