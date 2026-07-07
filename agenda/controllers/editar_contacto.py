import web
import sqlite3

render = web.template.render('views', base='layout')

class Editar_contacto:

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
        return render.editar_contacto(contacto)