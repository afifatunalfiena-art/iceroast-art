menu = {
    "Nasi Goreng": 12000,
    "Mie Ayam": 10000,
    "Sate Ayam": 20000,
    "Es Teh Manis": 3000,
    "Jus Jeruk": 5000
}

pesanan_pelanggan = {}

def tampilkan_menu():
    print("=" * 30)
    print("      MENU RESTORAN KAMI     ")
    print("=" * 30)
   
    for nama, harga in menu.items():
        print(f"{nama:<20} Rp {harga:,.0f}")
    print("=" * 30)

def ambil_pesanan():
    print("\n--- SILAKAN PESAN ---")   
    while True: #untuk perulangan yg benar
        nama_makanan = input("Masukkan nama makanan yang dipesan (ketik 'selesai' untuk Checkout): ").strip().title()        
        if nama_makanan == 'Selesai':
            break 
        if nama_makanan in menu:
            try:
                jumlah = int(input(f"Berapa porsi/gelas {nama_makanan} yang dipesan? "))              
                if jumlah <= 0:
                    print("Jumlah pesanan harus lebih dari nol.")
                    continue
                if nama_makanan in pesanan_pelanggan:
                    pesanan_pelanggan[nama_makanan] += jumlah
                else:
                    pesanan_pelanggan[nama_makanan] = jumlah
                    
                print(f"✅ {jumlah} {nama_makanan} telah ditambahkan ke pesanan.")
                
            except ValueError: #apabila nama menu tidak terdapat pada menu
                print("❌ Input jumlah tidak valid. Harap masukkan angka.")
        else:
            print(f"❌ '{nama_makanan}' tidak ada di menu kami. Mohon cek kembali.")

def cetak_struk():
    if not pesanan_pelanggan:
        print("\n=== TIDAK ADA PESANAN DIBUAT ===")
        return

    total_subtotal = 0
       
    print("\n" + "=" * 40)
    print("         STRUK PEMBELIAN RESTORAN      ")
    print("=" * 40)
    print(f"| {'Item':<20} | {'Qty':<5} | {'Harga Satuan':<10} | {'Subtotal':<10} |")
    print("-" * 40)
    for item, qty in pesanan_pelanggan.items():
        harga_satuan = menu[item]
        subtotal = harga_satuan * qty
        total_subtotal += subtotal
        print(f"| {item:<20} | {qty:<5} | {harga_satuan:,.0f} | {subtotal:,.0f} |")

    ppn_persen = 0.10
    ppn_nominal = total_subtotal * ppn_persen
    total_akhir = total_subtotal + ppn_nominal

    print("-" * 40)
    print(f"| {'Total Subtotal':<30} | Rp {total_subtotal:,.0f} |")
    print(f"| {'PPN (10%)':<30} | Rp {int(ppn_nominal):,.0f} |")
    print("=" * 40)
    print(f"| **TOTAL BAYAR**{'':<17} | **Rp {int(total_akhir):,.0f}** |")
    print("=" * 40)
    print("  TERIMA KASIH ATAS KUNJUNGAN ANDA!  ")
    print("=" * 40)

if __name__ == "__main__":
    tampilkan_menu()
    ambil_pesanan()
    cetak_struk()

