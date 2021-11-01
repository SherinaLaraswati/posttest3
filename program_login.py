ulang = "y"
percobaan = 0
username = ["null"]
password = ["null"]
user_admin = ["sherina laraswati"]
pass_admin = ["laarass"]
import os

def menu():
    print('=====================================')
    print('                MENU             ')
    print('=====================================')
    print('[1] Login\n[2] Sing in\n[3] Exit')
    print('=====================================')

def exit():
    print('=====================================')
    print('          TERIMA KASIH            ')
    print('=====================================')

def login(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    uname = str(input("Masukkan username anda: "))
    passw = str(input("Masukkan password anda: "))
    if uname in username and passw in password or uname in user_admin and passw in pass_admin:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Password benar\n")
        x = 0
        return x
    elif uname != username or passw != password:
        x += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("salah satu password atau username anda salah\n")
        print("sisa percobaan anda: ", x)
        return x
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Error.")
        exit()
        return x
        
while ulang == "y":
    menu()
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        percobaan += login(percobaan)
        ulang2 = int(input("Kembali ke menu?\n1. Ya\n2. Tidak\nPilihan: "))
        if ulang2 == 1:
            if percobaan < 3:
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Anda telah salah password sebanyak 3 kali. Akun anda telah direset.")
                username = ["null"]
                password = ["null"]
                break
        elif ulang2 == 2: 
            exit()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pilihan tidak valid.")
            exit()
            break
    elif pilihan == 2:
        if username == ["null"] and password == ["null"]:
            username = str(input("Masukkan username anda: "))
            password = str(input("Masukkan password anda: "))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Akun telah dibuat.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error. Anda telah memiliki Akun.")
    elif pilihan == 3:
        exit()
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pilihan tidak valid.")
        break