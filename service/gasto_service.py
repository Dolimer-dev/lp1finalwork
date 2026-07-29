from model.gasto import Gasto

class GastoService:
    def __init__(self, gasto_repository, categoria_repository):
        self.gasto_repository = gasto_repository
        self.categoria_repository = categoria_repository

    def crear_gasto(self, monto, fecha, categoria_uuid):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0")

        categoria = self.categoria_repository.obtener_por_uuid(categoria_uuid)
        if not categoria:
            raise ValueError("La categoría seleccionada no existe")

        nuevo_gasto = Gasto(monto, fecha, categoria_uuid)
        return self.gasto_repository.crear(nuevo_gasto)

    def listar_gastos(self):
        return self.gasto_repository.obtener_todos()

    def filtrar_por_categoria(self, categoria_uuid):
        return self.gasto_repository.obtener_por_categoria(categoria_uuid)

    def calcular_total(self):
        gastos = self.gasto_repository.obtener_todos()
        return sum(g.monto for g in gastos)

    def eliminar_gasto(self, gasto_uuid):
        return self.gasto_repository.eliminar(gasto_uuid)