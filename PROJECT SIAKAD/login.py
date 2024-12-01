import os
import pandas as pd
import time

def save_to_csv(username, password):
    file_path = r'datapassword.csv'
    data = {'Username': [username], 'Password': [password]}
    df = pd.DataFrame(data)
    df.to_csv(file_path, mode='a', header=False, index=False)

def check_login(username, password):
    file_path = r'datapassword.csv'
    df = pd.read_csv(file_path)
    user_data = df[df['Username'] == username]
    if not user_data.empty:
        stored_password = user_data['Password'].values[0]
        if stored_password == password:
            return True
        else:
            return False
    else:
        return False

def register_admin(): #[REGISTER DIUBAH KARENA DATA SUDAH DARI ADMIN]
    while True:
        print('=' * 50)
        print('Halaman Register ADMIN'.center(50))
        print('=' * 50)
        print('Silahkan membuat Username lalu masukkan password yang kuat')
        username = input('Masukkan Username : ')
        password = input('Masukkan Password : ')
    
        if len(password) < 8:
            print('ERROR : [MOHON MASUKKAN MINIMAL 8 KARAKTER!]')
            time.sleep(2) 
            clear_terminal()
            register_admin()
        else:
            save_to_csv(username, password)
            input('Akun berhasil dibuat, ketik ENTER untuk kembali ke menu utama')
            time.sleep(2) 
            clear_terminal()
            firstui()
            break

def login():
    while True:
        print('=' * 50)
        print('Halaman Login'.center(50))
        print('=' * 50)
        username = input('Masukkan Username: ').strip()
        password = input('Masukkan Password: ').strip()
        if check_login(username, password):
            print('Login Berhasil! Selamat Datang!')
            time.sleep(2) 
            clear_terminal()
            dashboard()
            break 
        else:
            print('Username atau Password salah. Coba lagi.')
            time.sleep(2) 
            clear_terminal()
            login()

def dashboard():
    clear_terminal()
    print('Halaman dashboard')

def clear_terminal():
    os.system('cls')

def firstui():
    print('=' * 50)
    print('SELAMAT DATANG DI SIAKAD, SILAHKAN PILIH MENU BERIKUT')
    print('=' * 50)
    print()
    print('1. Login')
    print('2. Keluar')
    print()
    print('=' * 50)
    choose = input('Masukkan Pilihan = ')
    
    if choose == '1':
        clear_terminal()
        login()
    elif choose == '2':
        print('END SESSION')
    else:
        clear_terminal()
        print('ERROR : [MOHON MASUKKAN INPUT YANG TEPAT]')
        firstui()

clear_terminal()   
firstui()