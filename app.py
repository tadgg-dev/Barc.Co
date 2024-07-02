from flask import Flask, render_template, request
from base_datos.conexion import Conexion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados', methods=['POST','GET'])
def resultados():
    dni = request.args.get('dni')
    usuario = request.args.get('usuario')
    contrasenna=request.args.get('password')
    conexion=Conexion('base_datos/usuarios.db')
    conexion.crear_tabla_cliente()
    if dni!=None and usuario!=None and contrasenna!=None:
        conexion.agregar_cliente(dni,usuario,contrasenna)
        clientes=conexion.mostrar_clientes()
        conexion.cerrar_conexion()
        
        return render_template('resultados.html', dni=dni, usuario=usuario,clientes=clientes)
    return render_template('index.html')    

@app.route("/editar/<id>", methods=['POST','GET'])
def editar(id):
    conexion=Conexion('base_datos/usuarios.db')
    cliente=conexion.obtener_cliente_x_id(id)
    conexion.cerrar_conexion
    return render_template('editar.html', cliente=cliente)

@app.route("/actualizar/<dni>", methods=['POST','GET'])
def actualizar(dni):
    dni=request.form.get('dni')
    usuario=request.form.get('usuario')
    contrasenna=request.form.get('password')
    conexion=Conexion('base_datos/usuarios.db')
    conexion.editar_cliente(dni,usuario,contrasenna)  
    clientes=conexion.mostrar_clientes()
    return render_template('resultados.html', clientes=clientes) 


@app.route("/eliminar",methods=['POST','GET'])
def eliminar():
    eliminar=request.args.get('eliminar')
    editar=request.args.get('editar')
    print(editar)
    print(eliminar)
    conexion=Conexion('base_datos/usuarios.db')
    if(eliminar!=None):        
        conexion.eliminar_cliente(eliminar)   
    
    clientes=conexion.mostrar_clientes()
    return render_template("resultados.html",clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)