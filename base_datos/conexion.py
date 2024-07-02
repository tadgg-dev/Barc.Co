import sqlite3


class Conexion:

  def __init__(self, nombre_bd):
    self.conexion = sqlite3.connect(nombre_bd)
    self.cursor = self.conexion.cursor()

  def crear_tabla_cliente(self):
    self.cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes(dni INT, usuario TEXT,contrasenna TEXT)")
    
    self.conexion.commit()

  def agregar_cliente(self, dni, usuario, contrasenna):
    self.cursor.execute("INSERT INTO clientes VALUES(?,?,?)",
                        (dni, usuario, contrasenna))
    self.conexion.commit()

  def editar_cliente(self, dni, usuario, contrasenna):
    self.cursor.execute(
        "UPDATE clientes SET dni=?, usuario=?, contrasenna=? WHERE dni=?",
        (dni, usuario, contrasenna,dni))
    self.conexion.commit()

  def mostrar_clientes(self):
    self.cursor.execute("SELECT * FROM clientes")
    clientes = self.cursor.fetchall()
    return clientes

  def eliminar_cliente(self, dni):
    self.cursor.execute("DELETE FROM clientes WHERE dni=?", (dni, ))
    self.conexion.commit()

  def obtener_cliente_x_id(self,id):
    self.cursor.execute("SELECT * FROM clientes WHERE dni=?", (id,))
    cliente=self.cursor.fetchone()
    return cliente

  def cerrar_conexion(self):
    self.cursor.close()
    self.conexion.close()
