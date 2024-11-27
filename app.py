from flask import *

import mysql.connector

# Conexion a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="iphone"
)
cursor = conexion.cursor()

app = Flask(__name__)

#página principal
@app.route('/')
def index():
  return render_template('index.html')

#menu pedidos
@app.route('/pedidos')
def pedidos():
  pass

#menu clientes
@app.route('/clientes')
def clientes():
  pass

#menu productos
@app.route('/productos')
def productos():
  query = "SELECT * FROM productos"
  cursor.execute(query)
  productos = cursor.fetchall()
  return render_template('productos.html',productos=productos)

@app.route('/agregar_productos')
def agregar_productos():
  pass

@app.route('/modificar_productos')
def modificar_productos():
  pass

@app.route('/eliminar_productos')
def eliminar_productos():
  pass


if __name__ == '__main__':
  app.run(debug=True)