import uuid

class Gasto:
    def __init__(self, monto, fecha, categoria_uuid):
        self.uuid = str(uuid.uuid4())
        self.monto = monto
        self.fecha = fecha
        self.categoria_uuid = categoria_uuid

    def __str__(self):
        return f"{self.fecha} - RD${self.monto} ({self.categoria_uuid})"