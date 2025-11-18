from decimal import Decimal
import random

random_decimal = Decimal(random.uniform(1.0, 10.0)).quantize(Decimal('0.01'))
print("Bilangan acak desimal:", random_decimal)
# Fungsi: Menghasilkan bilangan desimal acak dalam rentang tertentu.
# Kondisi: Ketika Anda perlu mensimulasikan angka desimal untuk pengujian.
