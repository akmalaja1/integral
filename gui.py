import tkinter as tk
from tkinter import messagebox
from main import hitung_integral

def hitung():
    fungsi = entry_fungsi.get()
    try:
        batas_bawah = float(entry_bawah.get())
        batas_atas = float(entry_atas.get())
        hasil = hitung_integral(fungsi, batas_bawah, batas_atas)
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Batas harus berupa angka valid.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Setup GUI
root = tk.Tk()
root.title("Kalkulator Integral")

tk.Label(root, text="Fungsi").grid(row=0, column=0, padx=10, pady=10)
entry_fungsi = tk.Entry(root, width=30)
entry_fungsi.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Batas Bawah").grid(row=1, column=0, padx=10, pady=10)
entry_bawah = tk.Entry(root, width=10)
entry_bawah.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Batas Atas").grid(row=2, column=0, padx=10, pady=10)
entry_atas = tk.Entry(root, width=10)
entry_atas.grid(row=2, column=1, padx=10, pady=10)

btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.grid(row=3, column=0, columnspan=2, pady=10)

label_hasil = tk.Label(root, text="Hasil: ")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
