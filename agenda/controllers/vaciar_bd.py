import web
import sqlite3

render = web.template.render('views', base='layout')

class Vaciar_bd:

    def vaciarBd(self) -> bool:
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()

            cursor.execute("DELETE FROM contactos;")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='contactos';")
            
            conn.commit()
            return True
            
        except sqlite3.Error as error:
            print(f"ERROR 111: {error.args}")
            return False
            
        except Exception as error:
            print(f"ERROR 112: {error.args}")
            return False
            
        finally:
            if conn:
                conn.close()

    def GET(self):
        return render.vaciar_bd()

    def POST(self):

        self.vaciarBd()
