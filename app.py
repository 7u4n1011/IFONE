from flask import *

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
  return render_template('productos.html')

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