from model.categoria import Categoria

class CategoriaService:
    def __init__(self, categoria_repository):
        self.categoria_repository = categoria_repository

    def crear_categoria(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre de la categoría no puede estar vacío")

        for categoria in self.categoria_repository.obtener_todas():
            if categoria.nombre.lower() == nombre.lower():
                raise ValueError("Ya existe una categoría con ese nombre")

        nueva_categoria = Categoria(nombre)
        return self.categoria_repository.crear(nueva_categoria)

    def listar_categorias(self):
        return self.categoria_repository.obtener_todas()

    def actualizar_categoria(self, categoria_uuid, nuevo_nombre):
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío")
        return self.categoria_repository.actualizar(categoria_uuid, nuevo_nombre)

    def eliminar_categoria(self, categoria_uuid):
        return self.categoria_repository.eliminar(categoria_uuid)