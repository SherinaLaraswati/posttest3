# ----------- DEKLARASI -----------------
harga_makanan = 0
harga_minuman = 0
total_harga = 0
import datetime #ambil nama hari ini
now = datetime.datetime.now()
import os
# ---------------------------------------

def function_makanan(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""------------- MENU MAKANAN ARASH CAFFE -------------
        1. kentang + chicken: Rp 20.000
        2. nasi + ayam penyet: Rp 16.000  
        3. mie goreng spesial: Rp 15.000
        4. seblak: Rp 15.000
        5. onion ring: Rp 15.000""")
    makanan = int(input("Pilihan: "))
    if makanan == 1:
        jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        if jumlah_makanan < 1:
            print("Jumlah tidak valid.")
            jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        elif jumlah_makanan >= 2:
            return (jumlah_makanan*20000)-((jumlah_makanan*20000)*0.05)
        else:
            return jumlah_makanan*20000
    elif makanan == 2:
        jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        if jumlah_makanan < 1:
            print("Jumlah tidak valid.")
            jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        elif jumlah_makanan >= 2:
            return (jumlah_makanan*16000)-((jumlah_makanan*16000)*0.05)
        else:
            return jumlah_makanan*16000
    elif makanan == 3:
        jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        if jumlah_makanan < 1:
            print("Jumlah tidak valid.")
            jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        elif jumlah_makanan >= 2:
            return (jumlah_makanan*15000)-((jumlah_makanan*15000)*0.05)
        else:
            return jumlah_makanan*15000
    elif makanan == 4:
        jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        if jumlah_makanan < 1:
            print("Jumlah tidak valid.")
            jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        elif jumlah_makanan >= 2:
            return (jumlah_makanan*15000)-((jumlah_makanan*15000)*0.05)
        else: 
            return jumlah_makanan*15000
    elif makanan == 5:
        jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        if jumlah_makanan < 1:
            print("Jumlah tidak valid.")
            jumlah_makanan = int(input("Jumlah porsi yang diinginkan: "))
        elif jumlah_makanan >= 2:
            return (jumlah_makanan*15000)-((jumlah_makanan*15000)*0.05)
        else:
            return  jumlah_makanan*15000
    else:
        print("Pilihan tidak valid.")

def function_minuman(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""------------- MENU MINUMAN ARASH CAFFE -------------
        1. chocolate: Rp 10.000
        2. air mineral: RP 5.000
        3. es kopi susu: Rp 11.000 
        4. americano: Rp 14.000
        5. green tea: Rp 13.000""")
    minuman = int(input("Pilihan: "))
    if minuman == 1:
        jumlah_minuman = int(input("Jumlah minuman yang diinginkan: "))
        if jumlah_minuman < 1:
            print("Jumlah tidak valid")
            jumlah_minuman = int(input("Jumlah minuman yang diingingkan: "))
        elif jumlah_minuman >= 3:
            return (jumlah_minuman*10000)-((jumlah_minuman*10000)*0.1)
        else:
            return jumlah_minuman*10000
    elif minuman == 2:
        jumlah_minuman = int(input("Jumlah minuman yang diinginkan: "))
        if jumlah_minuman < 1:
            print("Jumlah tidak valid")
            jumlah_minuman = int(input("Jumlah minuman yang diingingkan: "))
        elif jumlah_minuman >= 3:
            return (jumlah_minuman*5000)-((jumlah_minuman*5000)*0.1)
        else:
            return jumlah_minuman*5000
    elif minuman == 3:
        jumlah_minuman = int(input("Jumlah minuman yang diinginkan: "))
        if jumlah_minuman < 1:
            print("Jumlah tidak valid")
            jumlah_minuman = int(input("Jumlah minuman yang diingingkan: "))
        elif jumlah_minuman >= 3:
            return (jumlah_minuman*11000)-((jumlah_minuman*11000)*0.1)
        else:
            return jumlah_minuman*11000
    elif minuman == 4:
        jumlah_minuman = int(input("Jumlah minuman yang diinginkan: "))
        if jumlah_minuman < 1:
            print("Jumlah tidak valid")
            jumlah_minuman = int(input("Jumlah minuman yang diingingkan: "))
        elif jumlah_minuman >= 3:
            return (jumlah_minuman*14000)-((jumlah_minuman*14000)*0.1)
        else:
            return jumlah_minuman*14000
    elif minuman == 5:
        jumlah_minuman = int(input("Jumlah minuman yang diinginkan: "))
        if jumlah_minuman < 1:
            print("Jumlah tidak valid")
            jumlah_minuman = int(input("Jumlah minuman yang diingingkan: "))
        elif jumlah_minuman >= 3:
            return (jumlah_minuman*13000)-((jumlah_minuman*13000)*0.1)
        else:
            return jumlah_minuman*13000
    else:
        print("Pilihan tidak valid.")

def selamat_datang():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selamat datang di Arash Caffe\nHari ini, " + now.strftime("%A"))
    print("""
                            Arash Caffe
                               PROMO 
    A. setiap pembelian 3 minuman mendapatkan diskon sebesar 10%
    B. setiap pembelian 2 makanan mendapatkan diskon sebesar 5%
    C. setiap pembayaran melalui E-money mendapatkan diskon sebesar 5%
    D. pada saat weekend mendapatkan diskon sebesar 5%
    E. pada saat weekdays mendapatkan diskon sebesar 10%
    """)

selamat_datang()
pilihan = "y"
while pilihan =="y":

    pesan = int(input("Silahkan pilih kategori yang diinginkan:\n1. Makanan\n2. Minuman\nPilihan: "))
    if pesan == 1:
        harga_makanan += function_makanan(harga_makanan)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Total Harga makanan anda: ", harga_makanan)
    elif pesan == 2:
        harga_minuman += function_minuman(harga_minuman)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Total Harga minuman anda: ", harga_minuman)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pilihan tidak valid.")
        break
    pesan_lagi = int(input("Apakah ingin pesan lagi?\n1. Ya\n2. Tidak\nPilihan: "))
    if pesan_lagi == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        pilihan = "y"
    elif pesan_lagi == 2:
        total_harga = total_harga + harga_makanan + harga_minuman
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Total harga makanan anda: Rp. ", harga_makanan)
        print("Total harga minuman anda: Rp. ", harga_minuman)
        print("Total harga anda: Rp. ", total_harga)
        cara_bayar = int(input("Pilih metode pembayaran: \n1. Cash / Tunai\n2. E-Money\n Pilihan: "))
        if cara_bayar == 1:
            if now.strftime("%A") == "Saturday" or "Sunday":
                os.system('cls' if os.name == 'nt' else 'clear')
                total_harga -= total_harga*0.05
                print("Anda mendapat diskon Weekend sebesar 5%.\nTotal belanja anda sebesar: ", total_harga)
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                total_harga -= total_harga*0.1
                print("Anda mendapat diskon Weekdays sebesar 10%.\nTotal belanja anda sebesar: ", total_harga)
                break
        elif cara_bayar == 2:
            if now.strftime("%A") == "Saturday" or "Sunday":
                os.system('cls' if os.name == 'nt' else 'clear')
                total_harga -= (total_harga*0.05)*0.1
                print("Anda mendapat diskon Weekend sebesar 5% dan Diskon pembayaran E-Money sebesar 10%.\nTotal belanja anda sebesar: ", total_harga)
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                total_harga -= total_harga*0.1
                print("Anda mendapat diskon Weekdays sebesar 10% dan Diskon pembayaran E-Money sebesar 10%.\nTotal belanja anda sebesar: ", total_harga)
                break
    else:
        print("Pilihan tidak valid.")
        break