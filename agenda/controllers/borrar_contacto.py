import web
import sqlite3

render = web.template.render('views', base='layout')

class Borrar_contacto:

    def borrarContacto(self, contacto:dict)->bool:
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta el registro de la tabla contactos
            query = """
            DELETE FROM contactos
            WHERE id_contacto = ?;


            """
            cursor.execute(query, (contacto['id_contacto']))
            conn.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return False
        finally:
            if conn:
                conn.close()

    def editarContacto(self, id_contacto):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta el registro de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))            
            row = cursor.fetchone()
            
            if row:
                # Si encontró el registro, arma el diccionario
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                return contacto # Regresa el diccionario directo
            else:
                return {} # Si no hay resultados, regresa un diccionario vacío

        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return {}
        finally:
            if conn:
                conn.close()

    def GET(self, id_contacto):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.editarContacto(id_contacto)
        return render.borrar_contacto(contacto)
    
    def POST(self, id_contacto):
        formulario = web.input()
        contacto = {
            "id_contacto": formulario["id_contacto"],
            "nombre": formulario["nombre"],
            "primer_apellido": formulario["primer_apellido"],
            "segundo_apellido": formulario["segundo_apellido"],
            "email": formulario["email"],
            "telefono": formulario["telefono"],
        }
        resultado = self.borrarContacto(contacto)
        return resultado