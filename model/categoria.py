import uuid

class Categoria:
    def __init__(self, nombre):
        self.uuid = str(uuid.uuid4())
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"