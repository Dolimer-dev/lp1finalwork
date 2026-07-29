class GastoRepository:
    def __init__(self):
        self.gastos = []

    def crear(self, gasto):
        self.gastos.append(gasto)
        return gasto

    def obtener_todos(self):
        return self.gastos

    def obtener_por_uuid(self, gasto_uuid):
        for gasto in self.gastos:
            if gasto.uuid == gasto_uuid:
                return gasto
        return None

    def obtener_por_categoria(self, categoria_uuid):
        return [g for g in self.gastos if g.categoria_uuid == categoria_uuid]

    def eliminar(self, gasto_uuid):
        gasto = self.obtener_por_uuid(gasto_uuid)
        if gasto:
            self.gastos.remove(gasto)
            return True
        return False