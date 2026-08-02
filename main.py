from repository.categoria_repository import CategoriaRepository
from repository.gasto_repository import GastoRepository
from service.categoria_service import CategoriaService
from service.gasto_service import GastoService
from ui.app_window import AppWindow

def main():
    categoria_repository = CategoriaRepository()
    gasto_repository = GastoRepository()

    categoria_service = CategoriaService(categoria_repository, gasto_repository)
    gasto_service = GastoService(gasto_repository, categoria_repository)

    app = AppWindow(categoria_service, gasto_service)
    app.mainloop()

if __name__ == "__main__":
    main()