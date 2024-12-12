import sympy as sp

def hitung_integral(fungsi_str, batas_bawah, batas_atas):
    x = sp.Symbol('x')
    try:
        # Konversi string fungsi menjadi fungsi matematika
        fungsi = sp.sympify(fungsi_str)
        # Hitung integral
        hasil = sp.integrate(fungsi, (x, batas_bawah, batas_atas))
        return hasil
    except Exception as e:
        return f"Error: {e}"
