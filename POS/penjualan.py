import tkinter as tk
from tkinter import messagebox, ttk
import db

def penjualan_window():
    def refresh_penjualan():
        for row in tree.get_children():
            tree.delete(row)
        conn = db.get_connection()
        c = conn.cursor()
        c.execute("""
            SELECT p.id, b.nama, p.jumlah, p.total 
            FROM penjualan p
            JOIN barang b ON p.barang_id = b.id
            ORDER BY p.id DESC
            LIMIT 20
        """)
        rows = c.fetchall()
        conn.close()
        for row in rows:
            tree.insert("", "end", values=row)

    def jual():
        try:
            barang_id = int(entry_id.get())
            jumlah = int(entry_jumlah.get())
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("SELECT harga, stok FROM barang WHERE id=?", (barang_id,))
            result = c.fetchone()
            if not result:
                messagebox.showerror("Error", "Barang tidak ditemukan")
                return
            harga, stok = result
            if jumlah > stok:
                messagebox.showerror("Stok kurang", "Jumlah melebihi stok")
                return
            total = harga * jumlah
            c.execute("INSERT INTO penjualan (barang_id, jumlah, total) VALUES (?, ?, ?)",
                      (barang_id, jumlah, total))
            c.execute("UPDATE barang SET stok = stok - ? WHERE id = ?", (jumlah, barang_id))
            c.execute("INSERT INTO kas (tipe, jumlah, keterangan) VALUES ('pemasukan', ?, ?)",
                      (total, "Penjualan"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sukses", f"Penjualan berhasil dicatat.\nTotal: Rp {total}")
            entry_id.delete(0, tk.END)
            entry_jumlah.delete(0, tk.END)
            refresh_penjualan()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    win = tk.Toplevel()
    win.title("Penjualan")
    win.geometry("600x500")
    win.configure(bg="#f8f9fa")

    frame = tk.Frame(win, bg="white", padx=20, pady=20, bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.18, anchor="n", width=560)

    tk.Label(frame, text="Transaksi Penjualan", font=("Helvetica", 16, "bold"), bg="white").pack(pady=(0, 15))

    tk.Label(frame, text="ID Barang", font=("Helvetica", 10), bg="white").pack(anchor="w")
    entry_id = tk.Entry(frame, font=("Helvetica", 12))
    entry_id.pack(fill="x", pady=(0, 10))

    tk.Label(frame, text="Jumlah", font=("Helvetica", 10), bg="white").pack(anchor="w")
    entry_jumlah = tk.Entry(frame, font=("Helvetica", 12))
    entry_jumlah.pack(fill="x", pady=(0, 15))

    tk.Button(frame, text="Proses Penjualan", command=jual,
              bg="#28a745", fg="white", font=("Helvetica", 12),
              activebackground="#218838", bd=0, height=2)\
        .pack(fill="x")

    # Frame untuk list penjualan
    list_frame = tk.Frame(win, bg="white", bd=2, relief="groove")
    list_frame.place(relx=0.5, rely=0.5, anchor="n", width=560, height=250)

    tk.Label(list_frame, text="Riwayat Penjualan Terakhir", font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)

    columns = ("ID", "Nama Barang", "Jumlah", "Total (Rp)")
    tree = ttk.Treeview(list_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    refresh_penjualan()
