import sqlite3

def get_connection():
    conn = sqlite3.connect("db/kasir.db")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabel user
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Tabel barang
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS barang (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            stok INTEGER,
            harga INTEGER
        )
    """)

    # Tabel penjualan
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS penjualan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barang_id INTEGER,
            jumlah INTEGER,
            total INTEGER,
            tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabel kas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipe TEXT, -- pemasukan / pengeluaran
            jumlah INTEGER,
            keterangan TEXT,
            tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert user default
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
    except:
        pass

    conn.commit()
    conn.close()
