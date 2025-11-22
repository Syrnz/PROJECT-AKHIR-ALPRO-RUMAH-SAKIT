id_dokter = 1
dokter = {}

def tambah_data_dokter():

    global id_dokter
    while True:
        print("\n======================================================")
        input_nama_dokter = input("Masukkan nama dokter : ")
        if input_nama_dokter == "":
            print("INPUT TIDAK BOLEH KOSONG")
            continue
        cek_nama_dokter_duplikat = input_nama_dokter in dokter
        if cek_nama_dokter_duplikat:
            print("NAMA SUDAH TERDAFTAR!!")
            print("Silahkan masukkan nama lain.\n")
            continue

        # while True: 
        #     try:
        #         print("\n======================================================")
        #         input_umur_dokter = int(input("Masukkan Umur Dokter : "))
        #         if input_umur_dokter <= 16:
        #             print("UMUR DOKTER TIDAK VALID!!")
        #             continue
        #         break
        #     except:
        #         print("INPUT TIDAK VALID! INPUT HARUS ANGKA! ULANGI!")
        #         continue

        while True:
            try:
                print("\n======================================================")
                print("1. Spesialis Anak | 2. Spesialis Bedah | 3. Spesialis Jantung |")
                print("4. Spesialis Pembuluh darah | 5. Spesialis Kandungan |")
                print("6. Spesialis THT | 7. Spesialis Orang Dewasa | 8. Dokter UMUM |")
                print("===================== PILIH 1 - 8 ======================")
                input_spesialis_dokter = int(input("Masukkan Jenis Spesialis Dokter tersebut : "))
            except:
                print("INPUT TIDAK VALID! INPUT HARUS ANGKA! ULANGI!")
                continue
            if input_spesialis_dokter == 1:
                valid_spesialis_dokter = "Spesialis Anak"
                break
            elif input_spesialis_dokter == 2:
                valid_spesialis_dokter = "Spesialis Bedah"
                break
            elif input_spesialis_dokter == 3:
                valid_spesialis_dokter = "Spesialis Jantung"
                break
            elif input_spesialis_dokter == 4:
                valid_spesialis_dokter = "Spesialis Pembuluh darah"
                break
            elif input_spesialis_dokter == 5:
                valid_spesialis_dokter = "Spesialis Kandungan"
                break
            elif input_spesialis_dokter == 6:
                valid_spesialis_dokter = "Spesialis THT"
                break
            elif input_spesialis_dokter == 7:
                valid_spesialis_dokter = "Spesialis Orang Dewasa"
                break
            elif input_spesialis_dokter == 8:
                valid_spesialis_dokter = "Dokter Umum"
                break
            else:
                print("INPUT TIDAK VALID! PILIH DENGAN BENAR!")
                continue
                
        dokter[id_dokter] = input_nama_dokter, valid_spesialis_dokter
        print(dokter)
        id_dokter += 1
        print("")
        pilih = input("Tambah kontak lagi? (y): ").lower()
        if pilih == "y":
            continue
        else:
            break
    return


def lihat_semua_data_dokter():

    if not dokter:
        print("============ DATA DOKTER KOSONG! ============\n")
    else:
        print("============= List Data Dokter =============\n")
        for list_data_dokter in dokter:
            print(f"ID Dokter : {list_data_dokter} | Nama Dokter : {dokter[list_data_dokter][0]} | Bidang Medis : {dokter[list_data_dokter][1]} \n")
    
def cari_data_dokter():

    if not dokter:
        print("============ DATA DOKTER KOSONG! ============\n")

    cari_data = input("Masukkan Nama Dokter / Bidang Dokter yang ingin dicari : ").lower()
    ketemu = False

    for id_data_dokter, data_dokter in dokter.items():
        nama_dokter = data_dokter[0].lower()
        bidang_medis = data_dokter[1].lower()

        if cari_data in nama_dokter:
            if not ketemu:
                print("\n====== DATA DOKTER DITEMUKAN ======")
                ketemu = True
            print(f"ID Dokter : {id_data_dokter} | Nama Dokter : {data_dokter[0]} | Bidang Medis : {data_dokter[1]} | \n")

        elif cari_data in bidang_medis:
            if not ketemu:
                print("\n====== DATA DOKTER DITEMUKAN ======")
                ketemu = True
            print(f"ID Dokter : {id_dokter} | Nama Dokter : {data_dokter[0]} | Bidang Medis : {data_dokter[1]} | \n")

    if not ketemu:
        print("\nDOKTER TIDAK DITEMUKAN!\n")

    return

def lihat_data_dokter():
        
    while True:
        judul = "LIHAT DATA DOKTER"
        label = "PILIH 1-3"
        # label_judul1 = "=" * (len(judul) + 14)
        # label_judul2 = "=" * (len(label) + 10)
        # print(label_judul1)
        print(f"\n====== {judul} ======")
        print("|1. LIHAT SEMUA DATA          |")
        print("|2. CARI DATA                 |")
        print("|3. KEMBALI                   |")
        print(f"========== {label} ==========\n")
        # print(label_judul1)
        
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            lihat_semua_data_dokter()
        elif pilih == 2:
            cari_data_dokter()
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
        return

def update_data_nama_dokter():

    lihat_semua_data_dokter()

    try:
        cari_data_nama_dokter = input("Masukkan ID Dokter yang ingin dihapus : ").lower()
    except:
        print("INPUT HARUS ANGKA! ULANGI!")
    
    ketemu = False
    for id_data_dokter, data_dokter in dokter.items():
        nama_dokter = data_dokter[0].lower()
        bidang_medis = data_dokter[1].lower()
        if nama_dokter == cari_data_nama_dokter:
            while True:
                input_nama_dokter = input("Masukkan data baru nama dokter")
                if input_nama_dokter == "":
                    print("INPUT TIDAK BOLEH KOSONG")
                    continue
        cek_nama_dokter_duplikat = input_nama_dokter in dokter
        if cek_nama_dokter_duplikat:
            print("NAMA SUDAH TERDAFTAR!!")
            print("Silahkan masukkan nama lain.\n")
            continue

    return

def update_data_dokter():

    while True:
        judul = "UPDATE DATA DOKTER"
        label = "PILIH 1-3"
        # label_judul1 = "=" * (len(judul) + 14)
        # label_judul2 = "=" * (len(label) + 10)
        # print(label_judul1)
        print(f"\n====== {judul} ======")
        print("|1. UPDATE BERDASARKAN NAMA   |")
        print("|2. UPDATE BERDASARKAN BIDANG |")
        print("|3. KEMBALI                   |")
        print(f"========== {label} ==========\n")
        # print(label_judul1)
        
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            update_data_nama_dokter()
        elif pilih == 2:
            # update_data_bidang_dokter()
            pass
        elif pilih == 3:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue
        return
    return

def hapus_data_dokter():

    lihat_semua_data_dokter()

    try:
        cari_data_id = int(input("Masukkan ID Dokter yang ingin dihapus : "))
    except:
        print("INPUT HARUS ANGKA! ULANGI!")
    ketemu = False
    for id_data_dokter in dokter:
        if id_data_dokter == cari_data_id:
            if not ketemu:
                print("\n====== DATA DOKTER DITEMUKAN ======")
                ketemu = True
            (f"ID Dokter : {id_data_dokter} | Nama Dokter : {dokter[id_data_dokter][0]} | Bidang Medis : {dokter[id_data_dokter][1]}")
            hapus = input("Yakin ingin hapus data dokter ini? (y/n) : ")
            if hapus == "y":
                dokter.pop(id_data_dokter)
                print(f"data Dokter berhasil dihapus")
                break
            else:
                break
    if not ketemu:
        print("\nDOKTER TIDAK DITEMUKAN!\n")
    return

def main_dokter():
    while True:
        judul = "DATA DOKTER"
        label = "PILIH 1-5"
        label_judul1 = "=" * (len(judul) + 14)
        # label_judul2 = "=" * (len(label) + 10)
        print(label_judul1)
        print(f"====== {judul} ======")
        print("|1. TAMBAH DATA DOKTER  |")
        print("|2. LIHAT DATA DOKTER   |")
        print("|3. UPDATE DATA DOKTER  |")
        print("|4. HAPUS DATA DOKTER   |")
        print("|5. SELESAI             |")
        print(f"======= {label} =======")
        print(label_judul1)
    
        try:
            pilih = int(input(" Pilih Program : "))
        except:
            print("INPUT HARUS ANGKA! ULANGI!")
            continue
        if pilih == 1:
            tambah_data_dokter()
        elif pilih == 2:
            lihat_data_dokter()
        elif pilih == 3:
            pass
        elif pilih == 4:
            hapus_data_dokter()
        elif pilih == 5:
            break
        else:
            print("MASUKKAN PILIHAN YANG BENAR! ULANGI!")
            continue

