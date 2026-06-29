import web

render = web.template.render('views', base='layout')

class Lista_contacto:
    def GET(self):
        return render.lista_contacto()