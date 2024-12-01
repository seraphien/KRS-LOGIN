import os
import pandas as pd



def clear():
    os.system('cls')
    
# Fungsi menampilkan data

def tampilkan_data(nama_file, kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
        print(df)
    else:
        print(f"File {nama_file} tidak ditemukan. Belum ada data.")

# Fungsi menambah data

def tambah_data(nama_file, kolom):
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
    else:
        df = pd.DataFrame(columns=kolom)

    data_baru = {kol: input(f"Masukkan {kol}: ").strip() for kol in kolom}
    df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
    df.to_csv(nama_file, index=False)
    print("Data berhasil ditambahkan.")

# Fungsi mengedit data

def ubah_data(nama_file, kolom):
    clear()
    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan.")
        return

    df = pd.read_csv(nama_file)
    print(df)
    index = int(input("Masukkan nomor baris yang ingin diubah: "))
    if index < 0 or index >= len(df):
        print("Nomor baris tidak valid.")
        return

    for kol in kolom:
        nilai_baru = input(f"Masukkan {kol} baru (kosongkan untuk tetap): ").strip()
        if nilai_baru:
            df.at[index, kol] = nilai_baru

    df.to_csv(nama_file, index=False)
    print("Data berhasil diubah.")

# Fungsi menghapus data

def hapus_data(nama_file):
    clear()
    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan.")
        return

    df = pd.read_csv(nama_file)
    print(df)
    index = int(input("Masukkan nomor baris yang ingin dihapus: "))
    if index < 0 or index >= len(df):
        print("Nomor baris tidak valid.")
        return

    df = df.drop(index)
    df.to_csv(nama_file, index=False)
    print("Data berhasil dihapus.")

# Fungsi kelola data (umum)
def menu_kelola_data(menu_title, nama_file, kolom):
    clear()
    while True:
        print(f"\n--- {menu_title} ---")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            tampilkan_data(nama_file, kolom)
        elif pilihan == "2":
            tambah_data(nama_file, kolom)
        elif pilihan == "3":
            ubah_data(nama_file, kolom)
        elif pilihan == "4":
            hapus_data(nama_file)
        elif pilihan == "5":
            clear()
            print(f"Keluar dari menu {menu_title}.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi susun KRS

def susun_krs(file_krs):
    clear()
    file_matkul = "matkul.csv"
    file_kelas = "kelas.csv"

    if not os.path.exists(file_matkul) or not os.path.exists(file_kelas):
        print("File mata kuliah atau kelas tidak ditemukan.")
        return

    df_matkul = pd.read_csv(file_matkul)
    df_kelas = pd.read_csv(file_kelas)

    # Konversi kolom ke string
    df_matkul["Kode Mata Kuliah"] = df_matkul["Kode Mata Kuliah"].astype(str).str.strip()
    df_kelas["Kode Kelas"] = df_kelas["Kode Kelas"].astype(str).str.strip()

    print("\nDaftar Mata Kuliah:")
    print(df_matkul)
    print("\nDaftar Kelas:")
    print(df_kelas)

    kode_matkul = input("Masukkan kode mata kuliah: ").strip()
    kode_kelas = input("Masukkan kode kelas: ").strip()

    matkul = df_matkul[df_matkul["Kode Mata Kuliah"] == kode_matkul]
    kelas = df_kelas[df_kelas["Kode Kelas"] == kode_kelas]

    if matkul.empty or kelas.empty:
        print("Kode mata kuliah atau kelas tidak valid.")
        return

    hari = input("Masukkan hari: ").strip()
    jam = input("Masukkan jam: ").strip()

    data_krs = {
        "Kode Jadwal": f"{kode_matkul}-{kode_kelas}",
        "Hari": hari,
        "Mata Kuliah": matkul.iloc[0]["Nama Mata Kuliah"],
        "SKS": matkul.iloc[0]["SKS"],
        "Jam": jam,
        "Kelas": kelas.iloc[0]["Nama Kelas"],
    }

    if os.path.exists(file_krs):
        df_krs = pd.read_csv(file_krs)
    else:
        df_krs = pd.DataFrame(columns=data_krs.keys())

    df_krs = pd.concat([df_krs, pd.DataFrame([data_krs])], ignore_index=True)
    df_krs.to_csv(file_krs, index=False)
    print("KRS berhasil disusun.")

# Fungsi pilih KRS mahasiswa

def pilih_krs(file_admin_krs, file_mahasiswa_krs):
    clear()
    if not os.path.exists(file_admin_krs):
        print("Data KRS admin tidak ditemukan.")
        return

    df_admin_krs = pd.read_csv(file_admin_krs)
    print("\nDaftar Jadwal KRS:")
    print(df_admin_krs)

    kode_jadwal = input("Masukkan kode jadwal yang ingin dipilih: ").strip()

    jadwal = df_admin_krs[df_admin_krs["Kode Jadwal"].str.strip() == kode_jadwal]

    if jadwal.empty:
        print("Kode jadwal tidak valid.")
        return

    jadwal_data = jadwal.iloc[0]
    data_pilihan = {
        "Hari": jadwal_data["Hari"],
        "Mata Kuliah": jadwal_data["Mata Kuliah"],
        "SKS": jadwal_data["SKS"],
        "Jam": jadwal_data["Jam"],
        "Kelas": jadwal_data["Kelas"],
        "Kode Jadwal": jadwal_data["Kode Jadwal"],
    }

    if os.path.exists(file_mahasiswa_krs):
        df_mahasiswa_krs = pd.read_csv(file_mahasiswa_krs)
    else:
        df_mahasiswa_krs = pd.DataFrame(columns=data_pilihan.keys())

    df_mahasiswa_krs = pd.concat([df_mahasiswa_krs, pd.DataFrame([data_pilihan])], ignore_index=True)
    df_mahasiswa_krs.to_csv(file_mahasiswa_krs, index=False)
    print("KRS berhasil dipilih.")


def lihat_krs_mahasiswa(file_mahasiswa_krs):
    clear()
    # Periksa apakah file KRS mahasiswa sudah ada
    if not os.path.exists(file_mahasiswa_krs):
        print("Belum ada KRS yang dipilih.")
        return

    # Baca data KRS mahasiswa
    df_mahasiswa_krs = pd.read_csv(file_mahasiswa_krs)
    if df_mahasiswa_krs.empty:
        print("Belum ada KRS yang dipilih.")
    else:
        print("\nKRS yang telah dipilih:")
        print(df_mahasiswa_krs)


# Fungsi kelola KRS

def kelola_krs(menu_title, file_admin_krs, kolom_admin_krs):
    clear()
    file_mahasiswa_krs = "krs_mahasiswa.csv"
    while True:
        print(f"\n--- {menu_title} ---")
        print("1. Susun KRS")
        print("2. Tampilkan KRS Admin")
        print("3. Pilih KRS (Mahasiswa)")
        print("4. Keluar")
        print("5. Tampilkan krs")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            susun_krs(file_admin_krs)
        elif pilihan == "2":
            tampilkan_data(file_admin_krs, kolom_admin_krs)
        elif pilihan == "3":
            pilih_krs(file_admin_krs, file_mahasiswa_krs)
        elif pilihan == "5":
            lihat_krs_mahasiswa(file_mahasiswa_krs)
        elif pilihan == "4":
            print("Keluar dari menu Kelola KRS.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi utama
def main():
    clear()
    file_matkul = "matkul.csv"
    file_kelas = "kelas.csv"
    file_krs = "krs_admin.csv"

    kolom_matkul = ["Kode Mata Kuliah", "Nama Mata Kuliah", "SKS", "Jam Perkuliahan"]
    kolom_kelas = ["Kode Kelas", "Nama Kelas", "Ruang Kelas"]
    kolom_krs = ["Kode Jadwal", "Hari", "Mata Kuliah", "SKS", "Jam", "Kelas"]

    while True:
        print("\n--- Sistem Informasi Akademik ---")
        print("1. Kelola Mata Kuliah")
        print("2. Kelola Kelas")
        print("3. Kelola KRS")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_kelola_data("Kelola Mata Kuliah", file_matkul, kolom_matkul)
        elif pilihan == "2":
            menu_kelola_data("Kelola Kelas", file_kelas, kolom_kelas)
        elif pilihan == "3":
            kelola_krs("Kelola KRS", file_krs, kolom_krs)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem!")
            break
        else:
            print("Pilihan tidak valid.")

# Jal
if __name__ == "__main__":
    main()