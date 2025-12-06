# rumus

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def hitung_volume_tabung(jari_jari, tinggi):
    import math
    return math.pi * (jari_jari ** 2) * tinggi

import rumus

print("pilih perhitungan yang diinginkan:")
print("1. luas persegi panjang")
print("2. volume balok")
print("3. volume tabung")

pilihan = input("masukkan pilihan (1/2/3):")

if pilihan == '1':
    panjang = float(input("masukkan panjang:"))
    lebar = float(input("masukkan lebar:"))
    luas = rumus.hitung_luas_persegi_panjang(panjang, lebar)
    print(f"luas persegi panjang: {luas}")
elif pilihan == '2':
    panjang = float(input("masukkan panjang:"))
    lebar = float(input("masukkan lebar:"))
    tinggi = float(input("masukkan tinggi:"))
    volume = rumus.hitung_volume_balok(panjang, lebar, tinggi)
    print(f"volume balok : {volume}")
elif pilihan == '3':
    jari_jari = float(input("masukkan jari_jari:"))
    tinggi = float(input("masukkan tinggi:"))
    volume = rumus.hitung_volume_tabung(jari_jari, tinggi)
    print(f"volume balok : {volume}")
else:
    print("pilihan tidak valid. ")
