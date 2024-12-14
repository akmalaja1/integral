import sympy as sp
import ttkbootstrap as ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import Text
import time

# Fungsi untuk menghitung integral dengan langkah penyelesaian
def hitung_integral_dengan_langkah(fungsi, batas_bawah=None, batas_atas=None):
    x = sp.symbols('x')  # Mendefinisikan variabel simbolik
    try:
        # Mengubah fungsi input menjadi ekspresi simbolik
        fungsi_sympy = sp.sympify(fungsi)  # Gantilah eval dengan sympify untuk keamanan

        # Langkah 1: Memecah integral
        bagian_integral = fungsi.replace('-', '+-').split('+')  # Memisahkan berdasarkan '+' dan '-'
        langkah_1 = f"Integral: ∫({fungsi}) dx"
        langkah_1_detail = f"Memecah integral menjadi bagian-bagian:\n" + "\n".join([f"∫({bagian.strip()}) dx" for bagian in bagian_integral])

        # Langkah 2: Terapkan aturan integral pada masing-masing bagian
        langkah_2 = "Menerapkan aturan integral pada masing-masing bagian:"
        langkah_2_detail = []
        for bagian in bagian_integral:
            if 'x**2' in bagian:  # Untuk suku x^2
                langkah_2_detail.append(f"Integral dari {bagian}: ∫x^2 dx = (1/3)*x^3 + C")
            elif 'x' in bagian:  # Untuk suku x
                langkah_2_detail.append(f"Integral dari {bagian}: ∫x dx = (1/2)*x^2 + C")
            elif 'x' not in bagian:  # Untuk konstanta
                langkah_2_detail.append(f"Integral dari {bagian}: ∫(konstan) dx = konstan*x + C")
        
        langkah_2_full = "\n".join(langkah_2_detail)

        # Langkah 3: Gabungkan hasil integral
        integral_tak_tentu = sp.integrate(fungsi_sympy, x) + sp.symbols('C')  # Tambahkan konstanta integrasi
        langkah_3 = f"Integral tak tentu: ∫({fungsi}) dx = {integral_tak_tentu}"

        # Jika batas bawah dan atas tidak diberikan (integral tak tentu)
        if batas_bawah is None and batas_atas is None:
            return integral_tak_tentu, "\n".join([langkah_1, langkah_1_detail, langkah_2, langkah_2_full, langkah_3])

        # Langkah 4: Substitusi batas bawah dan atas untuk integral tentu
        nilai_integral = sp.integrate(fungsi_sympy, (x, batas_bawah, batas_atas))
        langkah_4 = f"Nilai integral tentu antara batas {batas_bawah} dan {batas_atas}: {nilai_integral}"

        # Gabungkan semua langkah
        langkah_lengkap = "\n".join([langkah_1, langkah_1_detail, langkah_2, langkah_2_full, langkah_3, langkah_4])
        return nilai_integral, langkah_lengkap

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

# Fungsi untuk tombol "Hitung"
def hitung():
    fungsi = entry_fungsi.get()
    try:
        batas_bawah = float(entry_bawah.get())
        batas_atas = float(entry_atas.get())
        
        # Menampilkan animasi fade
        label_hasil.config(text="Menghitung...", font=("Helvetica", 12))
        root.update_idletasks()  # Update GUI untuk menampilkan pesan

        # Simulasi animasi loading
        time.sleep(2)  # Durasi animasi loading
        
        # Menghitung integral dan langkah-langkah
        hasil, langkah = hitung_integral_dengan_langkah(fungsi, batas_bawah, batas_atas)
        
        # Tampilkan hasil dengan efek fade
        fade_in_label_hasil(hasil)
        
        # Menampilkan langkah-langkah penyelesaian satu per satu
        tampilkan_langkah_satu_per_satu(langkah)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def fade_in_label_hasil(hasil, step=5, max_alpha=255):
    """Fungsi untuk efek fade-in pada label hasil"""
    current_alpha = 0  # Mulai dengan transparansi 0 (transparan)
    label_hasil.config(text=f"Hasil: {hasil}")
    for alpha in range(0, max_alpha, step):
        # Mengubah warna teks dengan transparansi (dengan efek fade)
        hex_alpha = f"#{alpha:02x}{alpha:02x}{alpha:02x}"
        label_hasil.config(foreground=hex_alpha)
        root.after(20)  # Delay sebentar untuk efek animasi
        root.update_idletasks()  # Memperbarui tampilan GUI

def tampilkan_langkah_satu_per_satu(langkah, step=100):
    """Fungsi untuk menampilkan langkah penyelesaian satu per satu"""
    langkah_baris = langkah.split("\n")  # Memisahkan langkah-langkah berdasarkan baris
    for i, baris in enumerate(langkah_baris):
        root.after(i * step, update_text_langkah, baris)  # Menampilkan baris secara bertahap

def update_text_langkah(baris):
    """Fungsi untuk menambahkan baris ke textbox langkah"""
    text_langkah.insert(tk.END, baris + "\n")
    text_langkah.see(tk.END)  # Scroll ke bawah otomatis

# Setup GUI
root = ttk.Window(themename="darkly")  # Menggunakan Window dari ttkbootstrap untuk tema
root.title("Kalkulator Integral dengan Langkah Penyelesaian")
root.geometry("800x600")

# Konfigurasi grid utama
root.columnconfigure(0, weight=1)  # Kolom tengah
root.rowconfigure(0, weight=1)     # Baris tengah

# Frame utama
frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Konfigurasi grid di dalam frame
frame.columnconfigure(0, weight=1)  # Kolom kiri
frame.columnconfigure(1, weight=2)  # Kolom kanan
for i in range(7):  # Untuk semua baris
    frame.rowconfigure(i, weight=1)

# Instruksi dan format 
label_instruksi = ttk.Label(
    frame, 
    text="Contoh Soal: Hitung integral dari 3*x**2 + 2*x - 5 dengan batas bawah 1 dan batas atas 4",
    font=("Helvetica", 10)
)
label_instruksi.grid(row=0, column=0, columnspan=2, pady=5, sticky="n")

# Input fungsi
ttk.Label(frame, text="Fungsi", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_fungsi = ttk.Entry(frame, width=30, font=("Helvetica", 12))
entry_fungsi.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Input batas bawah
ttk.Label(frame, text="Batas Bawah", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_bawah = ttk.Entry(frame, width=10, font=("Helvetica", 12))
entry_bawah.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Input batas atas
ttk.Label(frame, text="Batas Atas", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_atas = ttk.Entry(frame, width=10, font=("Helvetica", 12))
entry_atas.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Tombol hitung
btn_hitung = ttk.Button(frame, text="Hitung", command=hitung, bootstyle="success")  # Gaya tombol 'success'
btn_hitung.grid(row=4, column=0, columnspan=2, pady=20)

# Label hasil
label_hasil = ttk.Label(frame, text="Hasil: ", font=("Helvetica", 12))
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

# Textbox untuk langkah penyelesaian
text_langkah = ttk.Text(frame, font=("Helvetica", 10), height=15, width=70, wrap="word")
text_langkah.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop()
