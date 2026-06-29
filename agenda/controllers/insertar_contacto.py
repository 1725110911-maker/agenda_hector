import web

render = web.template.render('views', base='layout')

class Insertar_contacto:
    def GET(self):
        return render.insertar_contacto()