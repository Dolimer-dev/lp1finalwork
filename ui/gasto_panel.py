import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

class GastoPanel(ttk.Frame):
    def __init__(self, parent, gasto_service, categoria_service):
        super().__init__(parent)
        self.gasto_service = gasto_service
        self.categoria_service = categoria_service

        self._crear_widgets()
        self._cargar_categorias_combobox()
        self._cargar_gastos()

    def _crear_widgets(self):
        frame_formulario = ttk.LabelFrame(self, text="Nuevo Gasto")
        frame_formulario.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_formulario, text="Monto:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_monto = ttk.Entry(frame_formulario)
        self.entry_monto.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_formulario, text="Fecha (YYYY-MM-DD):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_fecha = ttk.Entry(frame_formulario)
        self.entry_fecha.insert(0, str(date.today()))
        self.entry_fecha.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_formulario, text="Categoría:").grid(row=0, column=4, padx=5, pady=5)
        self.combo_categoria = ttk.Combobox(frame_formulario, state="readonly")
        self.combo_categoria.grid(row=0, column=5, padx=5, pady=5)

        btn_agregar = ttk.Button(frame_formulario, text="Agregar", command=self._agregar_gasto)
        btn_agregar.grid(row=0, column=6, padx=5, pady=5)

        frame_filtro = ttk.Frame(self)
        frame_filtro.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_filtro, text="Filtrar por categoría:").pack(side="left", padx=5)
        self.combo_filtro = ttk.Combobox(frame_filtro, state="readonly")
        self.combo_filtro.pack(side="left", padx=5)
        self.combo_filtro.bind("<<ComboboxSelected>>", lambda e: self._cargar_gastos())

        btn_quitar_filtro = ttk.Button(frame_filtro, text="Ver todos", command=self._quitar_filtro)
        btn_quitar_filtro.pack(side="left", padx=5)

        self.tree = ttk.Treeview(self, columns=("monto", "fecha", "categoria"), show="headings")
        self.tree.heading("monto", text="Monto")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("categoria", text="Categoría")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.label_total = ttk.Label(self, text="Total: RD$0", font=("Arial", 12, "bold"))
        self.label_total.pack(pady=5)

    def _cargar_categorias_combobox(self):
        categorias = self.categoria_service.listar_categorias()
        self.mapa_categorias = {c.nombre: c.uuid for c in categorias}

        nombres = list(self.mapa_categorias.keys())
        self.combo_categoria["values"] = nombres
        self.combo_filtro["values"] = ["Todas"] + nombres

    def _agregar_gasto(self):
        try:
            monto = float(self.entry_monto.get())
            fecha = self.entry_fecha.get()
            nombre_categoria = self.combo_categoria.get()

            if not nombre_categoria:
                messagebox.showerror("Error", "Selecciona una categoría")
                return

            categoria_uuid = self.mapa_categorias[nombre_categoria]
            self.gasto_service.crear_gasto(monto, fecha, categoria_uuid)

            self.entry_monto.delete(0, tk.END)
            self._cargar_gastos()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def _quitar_filtro(self):
        self.combo_filtro.set("")
        self._cargar_gastos()

    def _cargar_gastos(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        filtro = self.combo_filtro.get()
        if filtro and filtro != "Todas":
            categoria_uuid = self.mapa_categorias[filtro]
            gastos = self.gasto_service.filtrar_por_categoria(categoria_uuid)
        else:
            gastos = self.gasto_service.listar_gastos()

        categorias = {c.uuid: c.nombre for c in self.categoria_service.listar_categorias()}

        for gasto in gastos:
            nombre_categoria = categorias.get(gasto.categoria_uuid, "Desconocida")
            self.tree.insert("", tk.END, iid=gasto.uuid,
                            values=(gasto.monto, gasto.fecha, nombre_categoria))

        total = self.gasto_service.calcular_total()
        self.label_total.config(text=f"Total: RD${total}")