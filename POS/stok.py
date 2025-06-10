import tkinter as tk
from tkinter import ttk, messagebox
import db

def stok_window():
    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        conn = db.get_connection()
        c = conn.cursor()
        c.execute("SELECT id, nama, stok, harga FROM barang")
        rows = c.fetchall()
        for row in rows:
            tree.insert('', 'end', values=row)
        conn.close()

    def tambah_barang():
        try:
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO barang (nama, stok, harga) VALUES (?, ?, ?)",
                      (entry_nama.get(), int(entry_stok.get()), int(entry_harga.get())))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sukses", "Barang ditambahkan")
            entry_nama.delete(0, tk.END)
            entry_stok.delete(0, tk.END)
            entry_harga.delete(0, tk.END)
            load_data()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambah barang: {e}")

    win = tk.Toplevel()
    win.title("Manajemen Stok Barang")
    win.geometry("600x500")
    win.resizable(False, False)

    frame_form = tk.LabelFrame(win, text="Tambah Barang", padx=10, pady=10)
    frame_form.pack(padx=10, pady=10, fill="x")

    tk.Label(frame_form, text="Nama Barang").grid(row=0, column=0, sticky="w")
    entry_nama = tk.Entry(frame_form, width=30)
    entry_nama.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Stok").grid(row=1, column=0, sticky="w")
    entry_stok = tk.Entry(frame_form, width=30)
    entry_stok.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Harga").grid(row=2, column=0, sticky="w")
    entry_harga = tk.Entry(frame_form, width=30)
    entry_harga.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(frame_form, text="Tambah Barang", command=tambah_barang, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=10)

    # Table stok barang
    frame_table = tk.LabelFrame(win, text="Data Barang", padx=10, pady=10)
    frame_table.pack(padx=10, pady=10, fill="both", expand=True)

    columns = ("ID", "Nama", "Stok", "Harga")
    tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        if col == "ID":
            tree.column(col, width=50, anchor="center")
        else:
            tree.column(col, width=150, anchor="center")
    tree.pack(fill="both", expand=True)

    load_data()
