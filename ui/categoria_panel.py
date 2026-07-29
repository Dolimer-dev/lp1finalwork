import tkinter as tk
from tkinter import ttk, messagebox

class CategoriaPanel(ttk.Frame):
    def __init__(self, parent, categoria_service):
        super().__init__(parent)
        self.categoria_service = categoria_service

        self._crear_widgets()
        self._cargar_categorias()

    def _crear_widgets(self):
        frame_formulario = ttk.LabelFrame(self, text="Nueva Categoría")
        frame_formulario.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(frame_formulario)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        btn_agregar = ttk.Button(frame_formulario, text="Agregar", command=self._agregar_categoria)
        btn_agregar.grid(row=0, column=2, padx=5, pady=5)

        btn_eliminar = ttk.Button(self, text="Eliminar seleccionada", command=self._eliminar_categoria)
        btn_eliminar.pack(pady=5)

        self.tree = ttk.Treeview(self, columns=("nombre",), show="headings")
        self.tree.heading("nombre", text="Nombre")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def _agregar_categoria(self):
        nombre = self.entry_nombre.get()
        try:
            self.categoria_service.crear_categoria(nombre)
            self.entry_nombre.delete(0, tk.END)
            self._cargar_categorias()
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _eliminar_categoria(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una categoría primero")
            return

        categoria_uuid = seleccion[0]
        self.categoria_service.eliminar_categoria(categoria_uuid)
        self._cargar_categorias()

    def _cargar_categorias(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for categoria in self.categoria_service.listar_categorias():
            self.tree.insert("", tk.END, iid=categoria.uuid, values=(categoria.nombre,))