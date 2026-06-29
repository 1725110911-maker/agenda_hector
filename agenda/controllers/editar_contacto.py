import web

render = web.template.render('views', base='layout')

class Editar_contacto:
    def GET(self):
        return render.editar_contacto()