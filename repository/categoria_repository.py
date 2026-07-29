class CategoriaRepository:
    def __init__(self):
        self.categorias = []

    def crear(self, categoria):
        self.categorias.append(categoria)
        return categoria

    def obtener_todas(self):
        return self.categorias

    def obtener_por_uuid(self, categoria_uuid):
        for categoria in self.categorias:
            if categoria.uuid == categoria_uuid:
                return categoria
        return None

    def actualizar(self, categoria_uuid, nuevo_nombre):
        categoria = self.obtener_por_uuid(categoria_uuid)
        if categoria:
            categoria.nombre = nuevo_nombre
            return categoria
        return None

    def eliminar(self, categoria_uuid):
        categoria = self.obtener_por_uuid(categoria_uuid)
        if categoria:
            self.categorias.remove(categoria)
            return True
        return False