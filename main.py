from integral_utility import hitung_integral_dengan_langkah

# Fungsi yang akan diintegralkan
fungsi = "3*x**2 + 2*x - 5"

# Kasus 1: Tanpa batas bawah dan batas atas (integral tak tentu)
result_tak_tentu = hitung_integral_dengan_langkah(fungsi)
print("Integral Tak Tentu:")
print(result_tak_tentu)

# Kasus 2: Dengan batas bawah dan batas atas (integral tentu)
batas_bawah = 1
batas_atas = 4
result_tentu = hitung_integral_dengan_langkah(fungsi, batas_bawah, batas_atas)
print("\nIntegral Tentu:")
print(result_tentu)
