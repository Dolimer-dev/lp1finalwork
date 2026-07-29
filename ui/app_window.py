import tkinter as tk
from tkinter import ttk
from ui.categoria_panel import CategoriaPanel
from ui.gasto_panel import GastoPanel

class AppWindow(tk.Tk):
    def __init__(self, categoria_service, gasto_service):
        super().__init__()
        self.title("Control de Gastos Personales")
        self.geometry("700x500")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        panel_categorias = CategoriaPanel(notebook, categoria_service)
        panel_gastos = GastoPanel(notebook, gasto_service, categoria_service)

        notebook.add(panel_categorias, text="Categorías")
        notebook.add(panel_gastos, text="Gastos")