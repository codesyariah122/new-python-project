import tkinter as tk
from tkinter import messagebox
import db

def pembukuan_window():
    def tambah_transaksi():
        try:
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO kas (tipe, jumlah, keterangan) VALUES (?, ?, ?)",
                      (var_tipe.get(), int(entry_jumlah.get()), entry_ket.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sukses", "Transaksi dicatat")
            entry_jumlah.delete(0, tk.END)
            entry_ket.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mencatat transaksi.\n{str(e)}")

    win = tk.Toplevel()
    win.title("Pembukuan Kas")
    win.geometry("500x400")
    win.configure(bg="#f8f9fa")

    # Frame Konten
    frame = tk.Frame(win, bg="white", padx=20, pady=20, bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Pembukuan Kas", font=("Helvetica", 16, "bold"), bg="white").pack(pady=(0, 20))

    var_tipe = tk.StringVar(value="pengeluaran")
    tk.Label(frame, text="Tipe", font=("Helvetica", 10), bg="white").pack(anchor="w")
    tk.OptionMenu(frame, var_tipe, "pemasukan", "pengeluaran").pack(fill="x", pady=(0, 10))

    tk.Label(frame, text="Jumlah", font=("Helvetica", 10), bg="white").pack(anchor="w")
    entry_jumlah = tk.Entry(frame, font=("Helvetica", 12))
    entry_jumlah.pack(fill="x", pady=(0, 10))

    tk.Label(frame, text="Keterangan", font=("Helvetica", 10), bg="white").pack(anchor="w")
    entry_ket = tk.Entry(frame, font=("Helvetica", 12))
    entry_ket.pack(fill="x", pady=(0, 20))

    tk.Button(frame, text="Catat", command=tambah_transaksi,
              bg="#007bff", fg="white", font=("Helvetica", 12),
              activebackground="#0056b3", bd=0, height=2)\
        .pack(fill="x")

