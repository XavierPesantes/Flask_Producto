from flask_restful import Resource
import json
import pyodbc

SQLAZURECONNSTR = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servprueba.database.windows.net;DATABASE=Prueba;UID=admin_prueba;PWD=cd9YKqAQ'

# Create connection to Azure SQL
conn = pyodbc.connect(SQLAZURECONNSTR)

# Product Class
class Producto(Resource):
    def get(self, producto_id):
        result = {}
        try:
            cursor = conn.cursor()
            if producto_id:  
                cursor.execute('SELECT * FROM productos WHERE id = ?', str(producto_id))
                columnas = [col[0] for col in cursor.description]
                result = [dict(zip(columnas, row)) for row in cursor.fetchall()]
            else:
                return 'Ingrese un ID', 400
            if result:
                result = json.loads(json.dumps(result))
            return result, 200                                
        except Exception as e:
            print(str(e))
            return str(e), 500
        finally:
            cursor.close()

class Productos(Resource):
    def get(self):
        result = {}
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM productos')
            columnas = [col[0] for col in cursor.description]
            result = [dict(zip(columnas, row)) for row in cursor.fetchall()]
            if result:
                result = json.loads(json.dumps(result))
            return result, 200              
        except Exception as e:
            print(str(e))
            return str(e), 500
        finally:
            cursor.close()
