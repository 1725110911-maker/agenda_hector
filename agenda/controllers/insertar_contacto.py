import web
import sqlite3

render = web.template.render('views', base='layout')

class Insertar_contacto:

    def insertarContacto(self, contacto:dict)->bool:
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            
            # Consulta el registro de la tabla contactos
            query = """
            INSERT INTO contactos (nombre, primer_apellido, segundo_apellido, email, telefono)
            VALUES (?, ?, ?, ?, ?)

            """
            datos = (contacto['nombre'],
                     contacto['primer_apellido'],
                     contacto['segundo_apellido'],
                     contacto['email'],
                     contacto['telefono'],
                
            )
            cursor.execute(query, (datos))
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


    def GET(self):
        return render.insertar_contacto()
    
    def POST(self):
        formulario = web.input()
        contacto = {
            "nombre": formulario["nombre"],
            "primer_apellido": formulario["primer_apellido"],
            "segundo_apellido": formulario["segundo_apellido"],
            "email": formulario["email"],
            "telefono": formulario["telefono"],
        }
        resultado = self.insertarContacto(contacto)
        return resultado
        