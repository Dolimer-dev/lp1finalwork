# Control de Gastos Personales

Aplicación de escritorio para registrar gastos personales organizados por categorías, desarrollada en Python con Tkinter, siguiendo una arquitectura por capas (model / repository / service / ui) con inyección de dependencias por constructor.

**Repositorio:** https://github.com/Dolimer-dev/lp1finalwork

## Integrantes del equipo

| Nombre | Matrícula |
|---|---|
| Dolimer Gabriel César Rincón | LR2025-02957 |
| Patria Santana Farías | LR-2024-02156 |
| Ángel Antonio Estrella Mejía | LR-2024-02042 |
| Eliza Díaz Rosario | LR-2025-04019 |
| Juan Alberto Muñoz del Rosario | LR-2025-03637 |

**Asignatura:** Lenguaje de Programación 1
**Profesor:** Jaime Vilorio Green

## Funcionalidades

- CRUD de categorías (crear, listar, eliminar)
- CRUD de gastos (crear, listar, eliminar)
- Filtrar gastos por categoría
- Cálculo automático del total de gastos
- Eliminación en cascada: al borrar una categoría, se eliminan automáticamente sus gastos asociados

## Estructura del proyecto

```
lp1finalwork/
├── main.py
├── requirements.txt
├── .gitignore
├── model/
│   ├── categoria.py
│   └── gasto.py
├── repository/
│   ├── categoria_repository.py
│   └── gasto_repository.py
├── service/
│   ├── categoria_service.py
│   └── gasto_service.py
└── ui/
    ├── app_window.py
    ├── categoria_panel.py
    └── gasto_panel.py
```

- **model/**: clases que representan las entidades (Categoria, Gasto).
- **repository/**: gestiona el almacenamiento de los datos en memoria (listas de Python).
- **service/**: contiene la lógica de negocio y las validaciones.
- **ui/**: interfaz gráfica desarrollada con Tkinter.
- **main.py**: punto de entrada del programa; crea las dependencias y arranca la aplicación.

## Requisitos previos

- Python 3.10 o superior instalado.
- En Linux, si Tkinter no viene incluido: `sudo apt install python3-tk`.

## Instrucciones de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Dolimer-dev/lp1finalwork.git
cd lp1finalwork
```

### 2. Crear y activar el entorno virtual

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

Al activarse correctamente, la terminal debe mostrar `(venv)` al inicio de la línea.

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python main.py
```

## Cómo usar la aplicación

1. En la pestaña **Categorías**, escribe un nombre y presiona "Agregar" para crear una categoría.
2. Cambia a la pestaña **Gastos**, completa el monto, la fecha (formato `YYYY-MM-DD`) y selecciona una categoría del combobox.
3. Presiona "Agregar" para registrar el gasto.
4. Puedes filtrar los gastos por categoría usando el combobox de filtro, o presionar "Ver todos" para quitar el filtro.
5. El total de todos los gastos se muestra al final de la tabla y se recalcula automáticamente.
6. Para eliminar un gasto o una categoría, selecciona la fila en la tabla correspondiente y presiona el botón "Eliminar".

## Notas técnicas

- Los datos se manejan en memoria (listas de Python), no se usa base de datos, tal como especifica el proyecto.
- Cada categoría y cada gasto tiene un identificador único (UUID) generado automáticamente.
- La comunicación entre capas se realiza mediante inyección de dependencias por constructor: cada clase recibe lo que necesita a través de su `__init__`, sin crear sus propias dependencias por dentro.
