from decimal import Decimal

principal = Decimal('1000.00')
rate = Decimal('0.05')  # 5% bunga
time = Decimal('2')  # 2 tahun
interest = principal * rate * time
total_amount = principal + interest
print("Total setelah 2 tahun dengan bunga 5%:", total_amount)
# Fungsi: Menghitung total jumlah setelah menerapkan bunga.
# Kondisi: Ketika Anda perlu menghitung total dan bunga pada simpanan atau pinjaman.
