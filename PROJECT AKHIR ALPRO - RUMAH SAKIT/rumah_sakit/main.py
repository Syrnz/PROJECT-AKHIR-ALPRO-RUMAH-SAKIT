from dokter import main_dokter

# dokter = {}
pasien = {}
kamar = {}
obat = {}
transaksi = {}

def main():
    while True:
        judul = "RUMAH SAKIT"
        label = "PILIH 1-6"
        label_judul1 = "=" * (len(judul) + 10)
        # label_judul2 = "=" * (len(label) + 10)
        print(label_judul1)
        print(f"==== {judul} ====")
        print("|1. DATA DOKTER     |")
        print("|2. DATA PASIEN     |")
        print("|3. DATA KAMAR INAP |")
        print("|4. DATA OBAT       |")
        print("|5. DATA TRANSAKSI  |")
        print("|6. SELESAI         |")
        print(f"===== {label} =====")
        print(label_judul1)

        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            main_dokter()
        elif pilih == 2:
            pass
        elif pilih == 3:
            pass
        elif pilih == 4:
            pass
        elif pilih == 5:
            pass
        elif pilih == 6:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue

main()