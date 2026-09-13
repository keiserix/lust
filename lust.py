import tkinter as tk
from tkinter import messagebox

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado

def procesar(accion):
    texto = entrada_texto.get("1.0", tk.END).strip()
    try:
        clave = int(entrada_clave.get())
    except ValueError:
        messagebox.showerror("Error", "La clave debe ser un número entero.")
        return
    
    if not texto:
        messagebox.showwarning("Atención", "Por favor, escribe un mensaje.")
        return

    if accion == "cifrar":
        resultado = cifrar_cesar(texto, clave)
    else:
        resultado = cifrar_cesar(texto, -clave)
        
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, resultado)

# --- Configuración de la Ventana ---
ventana = tk.Tk()
ventana.title("Mi Encriptador Seguro")
ventana.geometry("450x450")
ventana.resizable(False, False)

# Etiqueta y entrada de texto original
tk.Label(ventana, text="Escribe tu mensaje aquí:", font=("Arial", 10, "bold")).pack(pady=5)
entrada_texto = tk.Text(ventana, height=5, width=50)
entrada_texto.pack(pady=5)

# Entrada de la clave numérica
tk.Label(ventana, text="Clave numérica (Desplazamiento):", font=("Arial", 10)).pack(pady=5)
entrada_clave = tk.Entry(ventana, width=10, justify="center")
entrada_clave.insert(0, "5")  # Clave por defecto
entrada_clave.pack(pady=5)

# Botones de acción
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

btn_cifrar = tk.Button(marco_botones, text="🔒 Cifrar", bg="#4CAF50", fg="white", width=12, command=lambda: procesar("cifrar"))
btn_cifrar.pack(side=tk.LEFT, padx=10)

btn_descifrar = tk.Button(marco_botones, text="🔓 Descifrar", bg="#2196F3", fg="white", width=12, command=lambda: procesar("descifrar"))
btn_descifrar.pack(side=tk.LEFT, padx=10)

# Etiqueta y salida del resultado
tk.Label(ventana, text="Resultado:", font=("Arial", 10, "bold")).pack(pady=5)
salida_texto = tk.Text(ventana, height=5, width=50)
salida_texto.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
