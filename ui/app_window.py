import tkinter as tk
from tkinter import ttk
from ui.categoria_panel import CategoriaPanel
from ui.gasto_panel import GastoPanel

class AppWindow(tk.Tk):
    def __init__(self, categoria_service, gasto_service):
        super().__init__()
        self.title("Control de Gastos Personales")
        self.geometry("700x500")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.panel_categorias = CategoriaPanel(self.notebook, categoria_service)
        self.panel_gastos = GastoPanel(self.notebook, gasto_service, categoria_service)

        self.notebook.add(self.panel_categorias, text="Categorías")
        self.notebook.add(self.panel_gastos, text="Gastos")

        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    def _on_tab_changed(self, event):
        pestaña_actual = self.notebook.select()
        if pestaña_actual == str(self.panel_gastos):
            self.panel_gastos._cargar_categorias_combobox()
            self.panel_gastos._cargar_gastos()