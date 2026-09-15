import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


ARCHIVO_HISTORIAL = "historial.txt"
ARCHIVO_NOTAS = "notas.txt"

USUARIO = "ypin31"
CONTRASENA = "ypin31"


class Aplicacion:

    def __init__(self, root):
        self.root = root

        self.root.title("BCL Persistent")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.inicializar_archivos()
        self.mostrar_login()

    # ------------------------------------------
    # ARCHIVOS
    # ------------------------------------------

    def inicializar_archivos(self):

        if not os.path.exists(ARCHIVO_HISTORIAL):
            with open(
                ARCHIVO_HISTORIAL,
                "w",
                encoding="utf-8"
            ) as archivo:
                archivo.write(
                    "Las credenciales pueden ser cambiadas\n"
                )

        if not os.path.exists(ARCHIVO_NOTAS):
            with open(
                ARCHIVO_NOTAS,
                "w",
                encoding="utf-8"
            ) as archivo:
                archivo.write("")

    def guardar_historial(self, texto):

        fecha = datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

        with open(
            ARCHIVO_HISTORIAL,
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"[{fecha}] {texto}\n"
            )

    # ------------------------------------------
    # INTERFAZ
    # ------------------------------------------

    def limpiar_ventana(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ------------------------------------------
    # LOGIN
    # ------------------------------------------

    def mostrar_login(self):

        self.limpiar_ventana()

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="BCL Persistent",
            font=("Arial", 24, "bold")
        ).pack(pady=(0, 30))

        tk.Label(
            frame,
            text="Usuario"
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            frame,
            width=35
        )

        self.usuario_entry.pack(
            pady=(5, 15)
        )

        tk.Label(
            frame,
            text="Contraseña"
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            frame,
            width=35,
            show="*"
        )

        self.contrasena_entry.pack(
            pady=(5, 20)
        )

        tk.Button(
            frame,
            text="Iniciar sesión",
            width=30,
            command=self.comprobar_login
        ).pack()

        self.usuario_entry.focus()

        self.contrasena_entry.bind(
            "<Return>",
            lambda event: self.comprobar_login()
        )

    def comprobar_login(self):

        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        if (
            usuario == USUARIO
            and contrasena == CONTRASENA
        ):

            self.guardar_historial(
                "Inicio de sesión correcto"
            )

            self.mostrar_menu()

        else:

            self.guardar_historial(
                "Intento de inicio de sesión fallido"
            )

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

    # ------------------------------------------
    # MENÚ PRINCIPAL
    # ------------------------------------------

    def mostrar_menu(self):

        self.limpiar_ventana()

        tk.Label(
            self.root,
            text="BCL Persistent",
            font=("Arial", 24, "bold")
        ).pack(pady=35)

        tk.Button(
            self.root,
            text="Calculadora",
            width=30,
            height=2,
            command=self.mostrar_calculadora
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Bloc de notas",
            width=30,
            height=2,
            command=self.mostrar_bloc_notas
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Historial",
            width=30,
            height=2,
            command=self.mostrar_historial
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Cerrar sesión",
            width=30,
            height=2,
            command=self.mostrar_login
        ).pack(pady=8)

    # ------------------------------------------
    # CALCULADORA
    # ------------------------------------------

    def mostrar_calculadora(self):

        self.limpiar_ventana()

        tk.Label(
            self.root,
            text="Calculadora",
            font=("Arial", 22, "bold")
        ).pack(pady=25)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(
            frame,
            text="Primer número"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        numero1 = tk.Entry(
            frame,
            width=20
        )

        numero1.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Operación"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        operacion = tk.StringVar(
            value="+"
        )

        tk.OptionMenu(
            frame,
            operacion,
            "+",
            "-",
            "*",
            "/"
        ).grid(
            row=1,
            column=1
        )

        tk.Label(
            frame,
            text="Segundo número"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        numero2 = tk.Entry(
            frame,
            width=20
        )

        numero2.grid(
            row=2,
            column=1
        )

        resultado_label = tk.Label(
            self.root,
            text="Resultado:",
            font=("Arial", 14)
        )

        resultado_label.pack(
            pady=25
        )

        def calcular():

            try:

                n1 = float(
                    numero1.get()
                )

                n2 = float(
                    numero2.get()
                )

                op = operacion.get()

                if op == "+":
                    resultado = n1 + n2

                elif op == "-":
                    resultado = n1 - n2

                elif op == "*":
                    resultado = n1 * n2

                elif op == "/":

                    if n2 == 0:

                        messagebox.showerror(
                            "Error",
                            "No se puede dividir entre cero."
                        )

                        return

                    resultado = n1 / n2

                resultado_label.config(
                    text=f"Resultado: {resultado}"
                )

                self.guardar_historial(
                    f"Calculadora: "
                    f"{n1} {op} {n2} = {resultado}"
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Introduce números válidos."
                )

        tk.Button(
            self.root,
            text="Calcular",
            width=25,
            command=calcular
        ).pack()

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.mostrar_menu
        ).pack(pady=15)

    # ------------------------------------------
    # BLOC DE NOTAS
    # ------------------------------------------

    def mostrar_bloc_notas(self):

        self.limpiar_ventana()

        tk.Label(
            self.root,
            text="Bloc de notas",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        texto = tk.Text(
            self.root,
            width=75,
            height=16
        )

        texto.pack(
            padx=20
        )

        try:

            with open(
                ARCHIVO_NOTAS,
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

            texto.insert(
                "1.0",
                contenido
            )

        except FileNotFoundError:
            pass

        def guardar_nota():

            contenido = texto.get(
                "1.0",
                "end-1c"
            )

            with open(
                ARCHIVO_NOTAS,
                "w",
                encoding="utf-8"
            ) as archivo:

                archivo.write(
                    contenido
                )

            self.guardar_historial(
                "Bloc de notas actualizado"
            )

            messagebox.showinfo(
                "Bloc de notas",
                "Nota guardada correctamente."
            )

        tk.Button(
            self.root,
            text="Guardar",
            width=25,
            command=guardar_nota
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.mostrar_menu
        ).pack()

    # ------------------------------------------
    # HISTORIAL
    # ------------------------------------------

    def mostrar_historial(self):

        self.limpiar_ventana()

        tk.Label(
            self.root,
            text="Historial",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        texto = tk.Text(
            self.root,
            width=75,
            height=17,
            state="disabled"
        )

        texto.pack(
            padx=20
        )

        try:

            with open(
                ARCHIVO_HISTORIAL,
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

        except FileNotFoundError:

            contenido = "No existe historial."

        texto.config(
            state="normal"
        )

        texto.insert(
            "1.0",
            contenido
        )

        texto.config(
            state="disabled"
        )

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.mostrar_menu
        ).pack(pady=15)


# ------------------------------------------
# INICIO
# ------------------------------------------

root = tk.Tk()

app = Aplicacion(root)

root.mainloop()