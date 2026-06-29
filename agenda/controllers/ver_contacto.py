import web

render = web.template.render('views', base='layout')

class Ver_contacto:
    def GET(self):
        return render.ver_contacto()