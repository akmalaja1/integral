import tkinter as tk
from sympy import symbols, integrate
from sympy.parsing.sympy_parser import parse_expr

# Fungsi untuk menghitung integral
def hitung_integral():
    try:
        # Ambil input dari user
        fungsi = entry_fungsi.get()
        batas_bawah = float(entry_bawah.get())
        batas_atas = float(entry_atas.get())
        
        # Parse ekspresi string menjadi ekspresi sympy
        x = symbols('x')
        fungsi_parsed = parse_expr(fungsi)
        
        # Hitung integral
        hasil = integrate(fungsi_parsed, (x, batas_bawah, batas_atas))
        label_hasil.config(text=f"Hasil: {hasil}")
        
    except Exception as e:
        label_hasil.config(text="Error: Input tidak valid.")

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Kalkulator Integral")

# Layout
tk.Label(root, text="Fungsi:").grid(row=0, column=0)
entry_fungsi = tk.Entry(root, width=20)
entry_fungsi.grid(row=0, column=1)

tk.Label(root, text="Batas Bawah:").grid(row=1, column=0)
entry_bawah = tk.Entry(root, width=20)
entry_bawah.grid(row=1, column=1)

tk.Label(root, text="Batas Atas:").grid(row=2, column=0)
entry_atas = tk.Entry(root, width=20)
entry_atas.grid(row=2, column=1)

tk.Button(root, text="Hitung", command=hitung_integral).grid(row=3, column=0, columnspan=2)
label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.grid(row=4, column=0, columnspan=2)

root.mainloop()
