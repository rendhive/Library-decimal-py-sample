from decimal import Decimal

original_price = Decimal('100.00')
discount = Decimal('0.15')  # 15% diskon
final_price = original_price - (original_price * discount)
print("Harga setelah diskon 15%:", final_price)
# Fungsi: Menghitung harga setelah diskon.
# Kondisi: Saat menghitung harga jual dan penentuan diskon pada produk.
