from decimal import Decimal, getcontext

getcontext().prec = 4  # Mengatur presisi menjadi 4
result = Decimal('1.23456789') + Decimal('2.34567891')
print("Hasil penjumlahan dengan presisi 4:", result)
# Fungsi: Mengatur jumlah digit presisi yang digunakan untuk perhitungan.
# Kondisi: Ketika Anda ingin membatasi presisi pada hasil perhitungan untuk laporan atau tampilan.
