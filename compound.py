modal = 200000000
bunga = 0.1 #per tahun
akhir = 400000000
tahun = 0
#berapa tahun untuk mencapai 400 juta ?
while modal <= akhir:
    tahun = tahun+1
    modal = modal+(modal*bunga)

print (f"jadi lama waktu yang dibutuhkan adalah {tahun} tahun, dengan total uang akhir sebesar {modal} Rupiah")
