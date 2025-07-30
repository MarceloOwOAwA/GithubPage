import tkinter as tk
from tkinter import messagebox
import requests
import json

API_URL = "http://localhost:8000/auth/registro"  # Cambia si tu endpoint es distinto

def registrar_usuario():
    name = name_entry.get().strip()
    email = email_entry.get().strip().lower()  # Convertir a minúsculas
    password = password_entry.get().strip()
    number = phone_entry.get().strip()
    citycode = citycode_entry.get().strip()
    contrycode = contrycode_entry.get().strip()

    # Validación básica
    if not name or not email or not password or not number or not citycode or not contrycode:
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    payload = {
        "name": name,               # Nombre requerido en el esquema
        "email": email,
        "password": password,
        "phones": [
            {
                "number": number,
                "citycode": citycode,
                "contrycode": contrycode
            }
        ]
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, json.dumps(result, indent=4))
    except requests.exceptions.HTTPError as err:
        try:
            error_json = err.response.json()
            error_msg = error_json.get("mensaje", err.response.text)
        except Exception:
            error_msg = err.response.text
        messagebox.showerror("Error", f"HTTP error: {err.response.status_code} - {error_msg}")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", f"Conexión fallida: {err}")

# Interfaz
root = tk.Tk()
root.title("Registro de Usuario")

tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1)

tk.Label(root, text="Contraseña:").grid(row=2, column=0, sticky="e")
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=2, column=1)

tk.Label(root, text="Teléfono:").grid(row=3, column=0, sticky="e")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=3, column=1)

tk.Label(root, text="Código ciudad:").grid(row=4, column=0, sticky="e")
citycode_entry = tk.Entry(root, width=30)
citycode_entry.grid(row=4, column=1)

tk.Label(root, text="Código país:").grid(row=5, column=0, sticky="e")
contrycode_entry = tk.Entry(root, width=30)
contrycode_entry.grid(row=5, column=1)

tk.Button(root, text="Registrar", command=registrar_usuario).grid(row=6, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
