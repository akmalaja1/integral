import tkinter as tk
from tkinter import messagebox
from main import hitung_integral

# Fungsi untuk menghitung integral
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
root.geometry("500x300")  # Ukuran jendela yang lebih besar
root.config(bg="#f0f0f0")  # Warna latar belakang yang lebih terang

# Font untuk teks
font_label = ("Arial", 12, "bold")
font_button = ("Arial", 12, "bold")
font_result = ("Arial", 12, "italic")

# Label dan input untuk fungsi
tk.Label(root, text="Fungsi", font=font_label, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_fungsi = tk.Entry(root, width=30, font=("Arial", 12))
entry_fungsi.grid(row=0, column=1, padx=10, pady=10)

# Label dan input untuk batas bawah
tk.Label(root, text="Batas Bawah", font=font_label, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_bawah = tk.Entry(root, width=10, font=("Arial", 12))
entry_bawah.grid(row=1, column=1, padx=10, pady=10)

# Label dan input untuk batas atas
tk.Label(root, text="Batas Atas", font=font_label, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_atas = tk.Entry(root, width=10, font=("Arial", 12))
entry_atas.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung integral
btn_hitung = tk.Button(root, text="Hitung", command=hitung, font=font_button, bg="#4CAF50", fg="white", relief="raised", width=15)
btn_hitung.grid(row=3, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="Hasil: ", font=font_result, bg="#f0f0f0", fg="#333333")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menampilkan jendela
root.mainloop()
