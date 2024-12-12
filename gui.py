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

# Menyesuaikan ukuran jendela dengan ukuran layar
screen_width = root.winfo_screenwidth()  # Lebar layar
screen_height = root.winfo_screenheight()  # Tinggi layar

# Mengatur ukuran jendela agar 80% dari ukuran layar
root.geometry(f"{int(screen_width * 0.8)}x{int(screen_height * 0.8)}")

# Background warna gelap dengan efek cahaya
root.config(bg="#333333")  # Latar belakang gelap

# Frame untuk memusatkan elemen di tengah dan transparan dengan border-radius
frame = tk.Frame(root, bg="#1c1c1c", bd=10, relief="flat", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Font untuk teks
font_label = ("Helvetica", 14, "bold")
font_button = ("Helvetica", 14, "bold")
font_result = ("Helvetica", 14, "italic")

# Label dan input untuk fungsi
tk.Label(frame, text="Fungsi", font=font_label, bg="#1c1c1c", fg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_fungsi = tk.Entry(frame, width=30, font=("Helvetica", 12), bd=2, relief="solid", highlightbackground="#4CAF50", highlightthickness=2)
entry_fungsi.grid(row=0, column=1, padx=10, pady=10)

# Label dan input untuk batas bawah
tk.Label(frame, text="Batas Bawah", font=font_label, bg="#1c1c1c", fg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_bawah = tk.Entry(frame, width=10, font=("Helvetica", 12), bd=2, relief="solid", highlightbackground="#4CAF50", highlightthickness=2)
entry_bawah.grid(row=1, column=1, padx=10, pady=10)

# Label dan input untuk batas atas
tk.Label(frame, text="Batas Atas", font=font_label, bg="#1c1c1c", fg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_atas = tk.Entry(frame, width=10, font=("Helvetica", 12), bd=2, relief="solid", highlightbackground="#4CAF50", highlightthickness=2)
entry_atas.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menghitung integral dengan efek hover
def on_enter(e):
    btn_hitung['background'] = '#45a049'  # Warna lebih gelap saat hover

def on_leave(e):
    btn_hitung['background'] = '#4CAF50'  # Warna kembali normal saat tidak hover

btn_hitung = tk.Button(frame, text="Hitung", command=hitung, font=font_button, bg="#4CAF50", fg="white", relief="raised", width=15, height=2, bd=0)
btn_hitung.grid(row=3, column=0, columnspan=2, pady=20)

btn_hitung.bind("<Enter>", on_enter)
btn_hitung.bind("<Leave>", on_leave)

# Label untuk menampilkan hasil
label_hasil = tk.Label(frame, text="Hasil: ", font=font_result, bg="#1c1c1c", fg="#ffffff")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menampilkan jendela
root.mainloop()
