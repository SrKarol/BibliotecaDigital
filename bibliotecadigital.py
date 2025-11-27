import customtkinter as ctk
from PIL import Image
import json
import os


class BibliotecaDigital:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Biblioteca Digital - Sistema de Gestión")
        self.ventana.geometry("1200x800")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.color_principal = "#8B4513"
        self.color_secundario = "#D2691E"
        self.color_fondo = "#FFF8DC"
        self.color_acento = "#CD853F"
        self.archivo_json = "biblioteca.json"
        self.libros = []
        self.cargar_datos()
        self.crear_interfaz()

    def cargar_datos(self):
        if os.path.exists(self.archivo_json):
            try:
                with open(self.archivo_json, 'r', encoding='utf-8') as f:
                    self.libros = json.load(f)
            except:
                self.crear_datos_iniciales()
        else:
            self.crear_datos_iniciales()

    def crear_datos_iniciales(self):
        self.libros = [
            {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
            {"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
            {"id": 3, "titulo": "1984", "autor": "George Orwell"},
            {"id": 4, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"},
            {"id": 5, "titulo": "Rayuela", "autor": "Julio Cortázar"},
            {"id": 6, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón"},
            {"id": 7, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez"},
            {"id": 8, "titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez"},
            {"id": 9, "titulo": "Crimen y castigo", "autor": "Fiódor Dostoyevski"},
            {"id": 10, "titulo": "Orgullo y prejuicio", "autor": "Jane Austen"}
        ]
        self.guardar_datos()

    def guardar_datos(self):
        with open(self.archivo_json, 'w', encoding='utf-8') as f:
            json.dump(self.libros, f, ensure_ascii=False, indent=4)

    def crear_interfaz(self):
        self.frame_principal = ctk.CTkFrame(
            self.ventana,
            fg_color=self.color_fondo
        )
        self.frame_principal.pack(fill="both", expand=True, padx=10, pady=10)
        titulo_frame = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        titulo_frame.pack(pady=20)

        titulo_label = ctk.CTkLabel(
            titulo_frame,
            text="BIBLIOTECA DIGITAL",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color=self.color_principal
        )
        titulo_label.pack()

        subtitulo_label = ctk.CTkLabel(
            titulo_frame,
            text="Sistema de Gestión de Libros",
            font=ctk.CTkFont(size=16),
            text_color=self.color_secundario
        )
        subtitulo_label.pack()
        contenedor = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        contenedor.pack(fill="both", expand=True, padx=20, pady=10)

        self.crear_panel_formulario(contenedor)
        self.crear_panel_lista(contenedor)

    def crear_panel_formulario(self, parent):
        panel_formulario = ctk.CTkFrame(
            parent,
            fg_color="white",
            corner_radius=15,
            border_width=2,
            border_color=self.color_acento
        )
        panel_formulario.pack(side="left", fill="both", padx=(0, 10), pady=0)
        panel_formulario.pack_propagate(False)
        panel_formulario.configure(width=350)

        agregar_label = ctk.CTkLabel(
            panel_formulario,
            text="AGREGAR LIBRO",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.color_principal
        )
        agregar_label.pack(pady=(20, 15))

        ctk.CTkLabel(
            panel_formulario,
            text="Título:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.color_principal
        ).pack(anchor="w", padx=20, pady=(10, 5))

        self.entry_titulo = ctk.CTkEntry(
            panel_formulario,
            placeholder_text="Ingrese el título del libro",
            height=40,
            font=ctk.CTkFont(size=14),
            border_color=self.color_acento,
            border_width=2
        )
        self.entry_titulo.pack(padx=20, pady=(0, 10), fill="x")

        ctk.CTkLabel(
            panel_formulario,
            text="Autor:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.color_principal
        ).pack(anchor="w", padx=20, pady=(10, 5))

        self.entry_autor = ctk.CTkEntry(
            panel_formulario,
            placeholder_text="Ingrese el nombre del autor",
            height=40,
            font=ctk.CTkFont(size=14),
            border_color=self.color_acento,
            border_width=2
        )
        self.entry_autor.pack(padx=20, pady=(0, 15), fill="x")

        btn_agregar = ctk.CTkButton(
            panel_formulario,
            text="Agregar Libro",
            command=self.agregar_libro,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.color_principal,
            hover_color=self.color_secundario,
            corner_radius=10
        )
        btn_agregar.pack(padx=20, pady=10, fill="x")

        separador = ctk.CTkFrame(panel_formulario, height=2, fg_color=self.color_acento)
        separador.pack(fill="x", padx=20, pady=20)

        buscar_label = ctk.CTkLabel(
            panel_formulario,
            text="BUSCAR LIBRO",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.color_principal
        )
        buscar_label.pack(pady=(10, 15))

        self.entry_buscar = ctk.CTkEntry(
            panel_formulario,
            placeholder_text="Buscar por título o autor...",
            height=40,
            font=ctk.CTkFont(size=14),
            border_color=self.color_acento,
            border_width=2
        )
        self.entry_buscar.pack(padx=20, pady=10, fill="x")
        self.entry_buscar.bind("<KeyRelease>", lambda e: self.buscar_libros())

        separador2 = ctk.CTkFrame(panel_formulario, height=2, fg_color=self.color_acento)
        separador2.pack(fill="x", padx=20, pady=20)

        btn_eliminar = ctk.CTkButton(
            panel_formulario,
            text="Eliminar Seleccionado",
            command=self.eliminar_libro,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#DC143C",
            hover_color="#B22222",
            corner_radius=10
        )
        btn_eliminar.pack(padx=20, pady=10, fill="x")

        self.label_contador = ctk.CTkLabel(
            panel_formulario,
            text=f"Total de libros: {len(self.libros)}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.color_principal
        )
        self.label_contador.pack(pady=20)

    def crear_panel_lista(self, parent):
        panel_lista = ctk.CTkFrame(
            parent,
            fg_color="white",
            corner_radius=15,
            border_width=2,
            border_color=self.color_acento
        )
        panel_lista.pack(side="right", fill="both", expand=True, pady=0)

        titulo_lista = ctk.CTkLabel(
            panel_lista,
            text="CATÁLOGO DE LIBROS",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.color_principal
        )
        titulo_lista.pack(pady=20)
        frame_scroll = ctk.CTkFrame(panel_lista, fg_color="transparent")
        frame_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.scrollable_frame = ctk.CTkScrollableFrame(
            frame_scroll,
            fg_color=self.color_fondo,
            corner_radius=10,
            border_width=2,
            border_color=self.color_acento
        )
        self.scrollable_frame.pack(fill="both", expand=True)
        self.mostrar_libros()

    def mostrar_libros(self, libros_filtrados=None):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        libros_a_mostrar = libros_filtrados if libros_filtrados is not None else self.libros

        if not libros_a_mostrar:
            no_libros = ctk.CTkLabel(
                self.scrollable_frame,
                text="No hay libros",
                font=ctk.CTkFont(size=18),
                text_color=self.color_secundario
            )
            no_libros.pack(pady=50)
            return

        for libro in libros_a_mostrar:
            self.crear_item_libro(libro)

    def crear_item_libro(self, libro):
        item_frame = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color="white",
            corner_radius=10,
            border_width=2,
            border_color=self.color_acento,
            height=80
        )
        item_frame.pack(fill="x", padx=10, pady=5)
        item_frame.pack_propagate(False)
        contenido_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        contenido_frame.pack(fill="both", expand=True, padx=15, pady=10)

        titulo_label = ctk.CTkLabel(
            contenido_frame,
            text=f"{libro['titulo']}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.color_principal,
            anchor="w"
        )
        titulo_label.pack(anchor="w", pady=(0, 5))

        autor_label = ctk.CTkLabel(
            contenido_frame,
            text=f"Autor: {libro['autor']}",
            font=ctk.CTkFont(size=14),
            text_color=self.color_secundario,
            anchor="w"
        )
        autor_label.pack(anchor="w")
        def on_enter(e):
            item_frame.configure(border_color=self.color_principal, border_width=3)

        def on_leave(e):
            item_frame.configure(border_color=self.color_acento, border_width=2)

        def on_click(e):
            self.libro_seleccionado = libro
            for widget in self.scrollable_frame.winfo_children():
                if isinstance(widget, ctk.CTkFrame):
                    widget.configure(fg_color="white")
            item_frame.configure(fg_color=self.color_fondo)

        item_frame.bind("<Enter>", on_enter)
        item_frame.bind("<Leave>", on_leave)
        item_frame.bind("<Button-1>", on_click)

        for child in item_frame.winfo_children():
            child.bind("<Button-1>", on_click)
            for subchild in child.winfo_children():
                subchild.bind("<Button-1>", on_click)

    def agregar_libro(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()

        if not titulo or not autor:
            self.mostrar_mensaje("Error", "Por favor complete todos los campos")
            return

        nuevo_id = max([libro['id'] for libro in self.libros], default=0) + 1

        nuevo_libro = {
            "id": nuevo_id,
            "titulo": titulo,
            "autor": autor
        }

        self.libros.append(nuevo_libro)
        self.guardar_datos()
        self.entry_titulo.delete(0, 'end')
        self.entry_autor.delete(0, 'end')
        self.mostrar_libros()
        self.actualizar_contador()
        self.mostrar_mensaje("Exito", f"Libro '{titulo}' agregado correctamente")

    def eliminar_libro(self):
        if not hasattr(self, 'libro_seleccionado') or not self.libro_seleccionado:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione un libro primero")
            return

        titulo = self.libro_seleccionado['titulo']
        self.libros = [libro for libro in self.libros if libro['id'] != self.libro_seleccionado['id']]
        self.guardar_datos()

        self.libro_seleccionado = None
        self.mostrar_libros()
        self.actualizar_contador()
        self.mostrar_mensaje("Exito", f"Libro '{titulo}' eliminado correctamente")

    def buscar_libros(self):
        termino = self.entry_buscar.get().strip().lower()

        if not termino:
            self.mostrar_libros()
            return

        libros_filtrados = [
            libro for libro in self.libros
            if termino in libro['titulo'].lower() or termino in libro['autor'].lower()
        ]

        self.mostrar_libros(libros_filtrados)

    def actualizar_contador(self):
        self.label_contador.configure(text=f"Total de libros: {len(self.libros)}")

    def mostrar_mensaje(self, titulo, mensaje):
        dialogo = ctk.CTkToplevel(self.ventana)
        dialogo.title(titulo)
        dialogo.geometry("400x150")
        dialogo.resizable(False, False)
        dialogo.transient(self.ventana)
        dialogo.grab_set()
        ctk.CTkLabel(
            dialogo,
            text=mensaje,
            font=ctk.CTkFont(size=16),
            wraplength=350
        ).pack(pady=30)

        ctk.CTkButton(
            dialogo,
            text="Aceptar",
            command=dialogo.destroy,
            width=100
        ).pack(pady=10)

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = BibliotecaDigital()
    app.ejecutar()