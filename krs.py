import csv
import os
import pandas as pd
import time

def clear_terminal():
    os.system('cls')

mata_kuliah = {
    1: {"nama": "Matematika Dasar", "sks": 3},
    2: {"nama": "Algoritma dan Struktur Data", "sks": 3},
    3: {"nama": "Etika Profesi", "sks": 3},
    4: {"nama": "Matematika Dasar", "sks": 3},
    5: {"nama": "Pengantar Rekayasa Perangkat Lunak", "sks": 3},
    6: {"nama": "Matematika Diskrit", "sks": 3},
    7: {"nama": "Bahasa Indonesia", "sks": 2},
    8: {"nama": "Pendidikan Pancasila", "sks": 2},
}
data = [{"kode": kode, "nama": mk["nama"], "sks": mk["sks"]} for kode, mk in mata_kuliah.items()]
df = pd.DataFrame(data)

df.to_csv("mata_kuliah.csv", index=False)
print("\nData telah disimpan ke mata_kuliah.csv")

def tampilkan_mata_kuliah():
    print("Tabel Mata Kuliah")
    print(df.to_string(index=False))

def pilih_mata_kuliah():
    krs = []
    total_sks = 0
    while True:
        tampilkan_mata_kuliah()
        try:
            kode = int(input("\nPilih mata kuliah berdasarkan kode (0 untuk selesai): "))
            if kode == 0:
                break
            elif kode in mata_kuliah:
                clear_terminal()
                mata_kuliah_terpilih = mata_kuliah[kode]
                if total_sks + mata_kuliah_terpilih['sks'] <= 24:
                    if mata_kuliah_terpilih not in krs:
                        krs.append(mata_kuliah_terpilih)
                        total_sks += mata_kuliah_terpilih['sks']
                        print(f"[{mata_kuliah_terpilih['nama']} TELAH DITAMBAHKAN KE KRS ANDA]")
                        time.sleep(2)
                        clear_terminal
                    else:
                        input('Mata Kuliah Sudah Dipilih, Mohon tekan ENTER untuk melanjutkan')
                else:
                    print("Jumlah SKS Anda melebihi batas maksimal (24 SKS).")
            else:
                print("Kode mata kuliah tidak valid.")
        except ValueError:
            print("Masukkan kode yang valid.")
    
    return krs, total_sks

def simpan_krs(krs, total_sks, nama_file = r'krs.csv'):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Mata Kuliah', 'SKS'])
        for mk in krs:
            writer.writerow([mk['nama'], mk['sks']])
        writer.writerow(['Total SKS', total_sks])
    print(f"KRS Anda telah disimpan!")

def tampilkan_krs(krs, total_sks):
    print("\nKartu Rencana Studi (KRS) Anda:")
    for mk in krs:
        print(f"- {mk['nama']} (SKS: {mk['sks']})")
    print(f"Total SKS yang diambil: {total_sks} SKS")

def main():
    clear_terminal()
    print()
    print("Selamat datang di Program Kartu Rencana Studi (KRS)")
    krs, total_sks = pilih_mata_kuliah()
    tampilkan_krs(krs, total_sks)
    simpan_krs(krs, total_sks)
    n=input('Tekan ENTER untuk kembali')
    #PATH kembali ke dashboard

main()
