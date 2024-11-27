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

# -----------------------------------------------------------------------

# PAGINA PRINCIPAL
@app.route('/')
def index():
  return render_template('index.html')

# -----------------------------------------------------------------------

# Menu Pedidos
@app.route('/pedidos')
def pedidos():
  query = "SELECT * FROM pedido"
  cursor.execute(query)
  pedidos = cursor.fetchall()
  return render_template('pedidos.html',pedidos=pedidos)

@app.route('/agregar_pedido', methods=['POST'])
def agregar_pedido():
  #obtengo los datos del formulario
  fecha = request.form.get('fecha')
  cantidad = request.form.get('cantidad')
  direccion = request.form.get('direccion')
  nombre_producto = request.form.get('nombre_producto')
  ID_cliente = request.form.get('ID_cliente')

  #los agrego a la base de datos
  query = 'INSERT INTO pedido (fecha, cantidad, direccion, nombre_producto, ID_cliente) VALUES (%s, %s, %s, %s, %s)'
  cursor.execute(query, (tipo,descripcion,nombre_producto,precio,ID_cliente))
  conexion.commit()
  return redirect(url_for('productos'))

@app.route('/modificar_pedido')
def modificar_pedido():
  pass

@app.route('/eliminar_pedido')
def eliminar_pedido():
  pass

# -----------------------------------------------------------------------

# Menu Clientes
@app.route('/clientes')
def clientes():
  query = "SELECT * FROM cliente"
  cursor.execute(query)
  clientes = cursor.fetchall()
  return render_template('clientes.html',clientes=clientes)

@app.route('/agregar_clientes', methods=['POST'])
def agregar_clientes():
  #obtengo los datos del formulario
  nombre = request.form.get('nombre')
  direccion = request.form.get('direccion')
  DNI = request.form.get('DNI')

  #los agrego a la base de datos
  query = 'INSERT INTO cliente (nombre, direccion, DNI) VALUES (%s, %s, %s)'
  cursor.execute(query, (nombre, direccion, DNI))
  conexion.commit()
  return redirect(url_for('cliente'))

@app.route('/modificar_clientes')
def modificar_clientes():
  pass

@app.route('/eliminar_clientes')
def eliminar_clientes():
  pass

# -----------------------------------------------------------------------

# Menu Productos
@app.route('/productos')
def productos():
  query = "SELECT * FROM productos"
  cursor.execute(query)
  productos = cursor.fetchall()
  return render_template('productos.html',productos=productos)

@app.route('/agregar_productos', methods=['POST'])
def agregar_productos():
  #obtengo los datos del formulario
  tipo = request.form.get('tipo')
  descripcion = request.form.get('descripcion')
  precio = request.form.get('precio')

  #los agrego a la base de datos
  query = 'INSERT INTO productos (tipo, descripcion, precio) VALUES (%s, %s, %s)'
  cursor.execute(query, (tipo,descripcion,precio))
  conexion.commit()
  return redirect(url_for('productos'))

@app.route('/modificar_productos')
def modificar_productos():
  pass

@app.route('/eliminar_productos')
def eliminar_productos():
  pass

# -----------------------------------------------------------------------

if __name__ == '__main__':
  app.run(debug=True)