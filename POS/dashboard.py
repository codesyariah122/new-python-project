import tkinter as tk
import penjualan
import stok
import pembukuan

def dashboard_window():
    root = tk.Tk()
    root.title("Dashboard Kasir")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    title_label = tk.Label(root, text="Dashboard Kasir", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    title_label.pack(pady=20)

    button_style = {
        "font": ("Helvetica", 12),
        "width": 25,
        "height": 2,
        "bg": "#4CAF50",
        "fg": "white",
        "activebackground": "#45a049",
        "bd": 0
    }

    tk.Button(root, text="Penjualan", command=penjualan.penjualan_window, **button_style).pack(pady=5)
    tk.Button(root, text="Stok Barang", command=stok.stok_window, **button_style).pack(pady=5)
    tk.Button(root, text="Pembukuan Kas", command=pembukuan.pembukuan_window, **button_style).pack(pady=5)

    root.mainloop()
