from decimal import Decimal

current_salary = Decimal('50000.00')
raise_rate = Decimal('0.08')  # 8%
new_salary = current_salary + (current_salary * raise_rate)
print("Gaji baru setelah kenaikan 8%:", new_salary)
# Fungsi: Menghitung gaji baru setelah penerapan kenaikan persentase.
# Kondisi: Saat melakukan evaluasi terhadap kenaikan gaji karyawan.
