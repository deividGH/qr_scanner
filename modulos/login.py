import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self):
        self.usuario = None
        self.contraseña = None
        self.ventana = tk.Tk()
        self.ventana.title("Login QR Scanner")
        self.ventana.geometry("400x600")
        self.ventana.config(bg="#f2f2f2")

        titulo = tk.Label(self.ventana, text="Iniciar sesión", font=("Arial", 24, "bold"), bg="#f2f2f2")
        titulo.pack(pady=30)

        label_usuario = tk.Label(self.ventana, text="Usuario", font=("Arial", 14), bg="#f2f2f2")
        label_usuario.pack(pady=5)

        self.entry_usuario = tk.Entry(self.ventana, font=("Arial", 14), width=25, bd=2, relief="solid")
        self.entry_usuario.pack(pady=10)

        label_contraseña = tk.Label(self.ventana, text="Contraseña", font=("Arial", 14), bg="#f2f2f2")
        label_contraseña.pack(pady=5)

        self.entry_contraseña = tk.Entry(self.ventana, font=("Arial", 14), show="*", width=25, bd=2, relief="solid")
        self.entry_contraseña.pack(pady=10)

        boton_login = tk.Button(self.ventana, text="Ingresar", font=("Arial", 12), bg="#4CAF50", fg="white", width=25, height=2, 
                                command=self.realizar_login)
        boton_login.pack(pady=20)

        boton_outlook = tk.Button(self.ventana, text="Ingresar con Outlook", font=("Arial", 12), bg="#0078D4", fg="white", width=25, height=2, 
                                  command=self.login_outlook)
        boton_outlook.pack(pady=10)

        self.ventana.mainloop()

    def realizar_login(self):

        usuarios = {
            "datolozao@udistrital.edu.co": "1234",
            "u": "u",
            "lmlugof@udistrital.edu.co" : "1234",
            "lamontanor@udistrital.edu.co" : "1234"
        }

        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        if usuario in usuarios and usuarios[usuario] == contraseña:
            messagebox.showinfo("Login exitoso", f"¡Bienvenido, {usuario}!")
            self.usuario = usuario
            self.contraseña = contraseña
            self.ventana.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def login_outlook(self):
        messagebox.showinfo("Login Outlook", "Ingreso con Outlook simulado.")

def ejecutar_login():
    app = LoginApp()
    return app.usuario
