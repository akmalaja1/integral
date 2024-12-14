import sympy as sp
from sympy import symbols, integrate

def hitung_integral_dengan_langkah(fungsi, batas_bawah=None, batas_atas=None):
    x = symbols('x')  # Mendefinisikan variabel simbolik
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
        integral_tak_tentu = integrate(fungsi_sympy, x) + symbols('C')  # Tambahkan konstanta integrasi
        langkah_3 = f"Integral tak tentu: ∫({fungsi}) dx = {integral_tak_tentu}"

        # Jika batas bawah dan atas tidak diberikan (integral tak tentu)
        if batas_bawah is None and batas_atas is None:
            return integral_tak_tentu, "\n".join([langkah_1, langkah_1_detail, langkah_2, langkah_2_full, langkah_3])

        # Langkah 4: Substitusi batas bawah dan atas untuk integral tentu
        nilai_integral = integrate(fungsi_sympy, (x, batas_bawah, batas_atas))
        langkah_4 = f"Nilai integral tentu antara batas {batas_bawah} dan {batas_atas}: {nilai_integral}"

        # Gabungkan semua langkah
        langkah_lengkap = "\n".join([langkah_1, langkah_1_detail, langkah_2, langkah_2_full, langkah_3, langkah_4])
        return nilai_integral, langkah_lengkap

    except Exception as e:
        return f"Terjadi kesalahan: {e}"
