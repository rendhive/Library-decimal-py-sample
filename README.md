# Library-decimal-py-sample

# Aritmetika Desimal dengan Python `decimal` 🤓💰
Butuh akurasi tinggi buat hitung uang atau angka pecahan? Python punya modul `decimal` yang presisinya jauh lebih stabil daripada `float`. Cocok banget buat keuangan, laporan bisnis, atau perhitungan yang ga boleh meleset.

## 🚀 Daftar Isi
- [Instalasi](#instalasi)
- [Cara Pakai](#cara-pakai)
  - [Import Modul](#import-modul)
  - [Operasi Dasar](#operasi-dasar)
  - [Atur Presisi](#atur-presisi)
  - [Contoh Kode](#contoh-kode)
- [Kapan Dipakai](#kapan-dipakai)
- [Referensi](#referensi)

---

## 🔧 Instalasi
Tenang, ga perlu install apa-apa. Modul `decimal` **sudah bawaan Python** (sejak Python 2.4). Tinggal pakai aja.

---

## 🧪 Cara Pakai

### 1. Import Modul
Pilih salah satu cara berikut:

```python
from decimal import Decimal

atau:

import decimal

2. Operasi Dasar

Decimal bisa dipakai buat:

➕ Penjumlahan

➖ Pengurangan

✖️ Perkalian

➗ Pembagian


Semua dengan hasil yang lebih presisi dibanding float.

3. Atur Presisi

Kalau kamu butuh hasil super-rapi, atur presisinya:

from decimal import getcontext
getcontext().prec = 4  # presisi 4 digit

4. Contoh Kode Lengkap

from decimal import Decimal, getcontext

# Atur presisi
getcontext().prec = 4  

# Operasi dasar
a = Decimal('0.1')
b = Decimal('0.2')
result_sum = a + b
print("Hasil 0.1 + 0.2 =", result_sum)

# Hitung rata-rata
numbers = [Decimal('100.25'), Decimal('200.75'), Decimal('50.50')]
average = sum(numbers) / len(numbers)
print("Rata-rata:", average)

# Hitung diskon 15%
original_price = Decimal('100.00')
discount = Decimal('0.15')
final_price = original_price - (original_price * discount)
print("Harga setelah diskon:", final_price)


---

📝 Kapan Dipakai?

Gunakan decimal saat kamu butuh:

💵 Presisi tinggi untuk angka mata uang

📊 Perhitungan akuntansi & laporan keuangan

🧐 Hasil yang ga boleh meleset seperti float

🧪 Data ilmiah yang butuh pengendalian presisi



---

📚 Referensi

Dokumentasi resmi Python: decimal
(docs.python.org/3/library/decimal.html)
