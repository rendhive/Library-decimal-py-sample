from decimal import Decimal

gross_income = Decimal('4000.00')
tax_rate = Decimal('0.2')  # 20%
net_income = gross_income - (gross_income * tax_rate)
print("Penghasilan bersih setelah pajak 20%:", net_income)
# Fungsi: Menghitung penghasilan bersih setelah pengurangan pajak.
# Kondisi: Ketika Anda ingin mengetahui berapa yang akan diterima setelah pajak.
