from decimal import Decimal, ROUND_HALF_UP

value = Decimal('2.675')
rounded_value = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Pembulatan ke dua tempat desimal
print("Hasil pembulatan:", rounded_value)
# Fungsi: Menghitung hasil pembulatan angka desimal.
# Kondisi: Ketika Anda perlu menjaga presisi desimal dan ingin membulatkan nilai dengan cara tertentu.
