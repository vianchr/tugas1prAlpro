def keuntungan_jual(harga_awal, harga_jual, gram_awal):
    selisih = harga_jual * gram_awal - harga_awal * gram_awal
    selisih_persen = (selisih/(harga_awal*gram_awal)*100)
    return print(f"jadi keuntungannya adalah {selisih}\ndalam persen adalah {selisih_persen}%")
keuntungan_jual(650000,685000,25)

print()

def keuntungan_kedua(harga_1, harga_2, gram, tambahan , harga_3):
    keuntungan= (harga_3*(gram+tambahan))- (harga_1*gram + harga_2*tambahan)
    persen_untung = (keuntungan/(harga_1*gram + harga_2*tambahan)*100)
    return print(f"jadi keuntungan kedua adalah {keuntungan}\ndalam persen adalah {persen_untung}%")
keuntungan_kedua(650000,685000,25,15, 715000)
