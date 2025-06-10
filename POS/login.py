import tkinter as tk
from tkinter import messagebox
import db
import dashboard

def login_window():
    def attempt_login():
        conn = db.get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username.get(), password.get()))
        result = c.fetchone()
        conn.close()

        if result:
            root.destroy()
            dashboard.dashboard_window()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

    root = tk.Tk()
    root.title("Login Kasir")

    # ❗ Fullscreen atau ukuran tetap besar
    root.geometry("500x400")  # Atau pakai root.attributes('-zoomed', True) di Linux

    # Warna latar
    root.configure(bg="#f0f0f0")

    # Frame tengah untuk form
    form_frame = tk.Frame(root, bg="white", padx=30, pady=30, relief="ridge", bd=2)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(form_frame, text="Login Kasir", font=("Helvetica", 16, "bold"), bg="white").pack(pady=(0, 20))

    tk.Label(form_frame, text="Username", anchor="w", bg="white", font=("Helvetica", 10)).pack(fill='x')
    username = tk.Entry(form_frame, font=("Helvetica", 12))
    username.pack(fill='x', pady=(0, 10))

    tk.Label(form_frame, text="Password", anchor="w", bg="white", font=("Helvetica", 10)).pack(fill='x')
    password = tk.Entry(form_frame, show="*", font=("Helvetica", 12))
    password.pack(fill='x', pady=(0, 20))

    tk.Button(form_frame, text="Login", command=attempt_login,
              font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45a049", bd=0, height=2)\
        .pack(fill='x')

    root.mainloop()
