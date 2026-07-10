import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contacto', 'controllers.lista_contacto.Lista_contacto',
    '/ver_contacto/(\d+)', 'controllers.ver_contacto.Ver_contacto',
    '/insertar_contacto', 'controllers.insertar_contacto.Insertar_contacto',
    '/editar_contacto/(\d+)', 'controllers.editar_contacto.Editar_contacto',
    '/borrar_contacto/(\d+)', 'controllers.borrar_contacto.Borrar_contacto',
    '/vaciar_bd', 'controllers.vaciar_bd.Vaciar_bd'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()