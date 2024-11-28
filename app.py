from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iphone"
)
cursor = conexion.cursor()

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Menu Pedidos
@app.route('/pedidos')
def pedidos():
    query = "SELECT * FROM pedido"
    cursor.execute(query)
    pedidos = cursor.fetchall()
    return render_template('pedidos.html', pedidos=pedidos)

@app.route('/agregar_pedido', methods=['POST'])
def agregar_pedido():
    fecha = request.form.get('fecha')
    cantidad = request.form.get('cantidad')
    direccion = request.form.get('direccion')
    nombre_producto = request.form.get('nombre_producto')
    ID_cliente = request.form.get('ID_cliente')

    query = 'INSERT INTO pedido (fecha, cantidad, direccion, nombre_producto, ID_cliente) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(query, (fecha, cantidad, direccion, nombre_producto, ID_cliente))
    conexion.commit()
    return redirect(url_for('pedidos'))

# Menu Clientes
@app.route('/clientes')
def clientes():
    query = "SELECT * FROM cliente"
    cursor.execute(query)
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)

@app.route('/agregar_clientes', methods=['POST'])
def agregar_clientes():
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    DNI = request.form.get('DNI')

    query = 'INSERT INTO cliente (nombre, direccion, DNI) VALUES (%s, %s, %s)'
    cursor.execute(query, (nombre, direccion, DNI))
    conexion.commit()
    return redirect(url_for('clientes'))

# Menu Productos
@app.route('/productos')
def productos():
    query = "SELECT * FROM productos"
    cursor.execute(query)
    productos = cursor.fetchall()
    return render_template('productos.html', productos=productos)

@app.route('/agregar_productos', methods=['POST'])
def agregar_productos():
    tipo = request.form.get('tipo')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')

    query = 'INSERT INTO productos (tipo, descripcion, precio) VALUES (%s, %s, %s)'
    cursor.execute(query, (tipo, descripcion, precio))
    conexion.commit()
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)
