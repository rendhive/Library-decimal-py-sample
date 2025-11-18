from decimal import Decimal

sales = Decimal('15000.00')
commission_rate = Decimal('0.1')  # 10%
commission = sales * commission_rate
print("Komisi dari penjualan:", commission)
# Fungsi: Menghitung jumlah komisi berdasarkan nilai penjualan.
# Kondisi: Ketika menghitung bonus atau komisi bagi tenaga penjual.
