from decimal import Decimal

value = Decimal('1234.56')
with open('output.txt', 'w') as file:
    file.write(str(value))

print("Angka desimal telah disimpan ke file output.txt.")
# Fungsi: Menyimpan angka desimal ke dalam file sebagai data teks.
# Kondisi: Ketika Anda perlu menyimpan hasil perhitungan ke dalam file untuk analisis lebih lanjut.
