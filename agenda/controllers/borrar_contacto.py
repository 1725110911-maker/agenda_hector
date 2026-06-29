import web

render = web.template.render('views', base='layout')

class Borrar_contacto:
    def GET(self):
        return render.borrar_contacto()