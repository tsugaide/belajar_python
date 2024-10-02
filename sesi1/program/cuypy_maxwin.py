
import random
import main
def start():
    
    print("========================")
    print("== Welcome Lost Young ==")
    print("========================")
    koin = 50

    while True:
        angka_random = random.randint(1, 4)
        jakpot = angka_random
        
        bentuk_kotak = "|_|"
        kotak_kosong = [bentuk_kotak] * 4
        kotak = kotak_kosong.copy()
        kotak[jakpot-1] = f"|*{jakpot}*|"
        kotak = '-'.join(kotak)
        
        
        print(f"\n\nkoinmu adalah {koin}")
        jumlah_depo = int(input("\nMasukkan koin, jika kamu benar koin yang kamu masukkan akan digandakan: "))
        
        while jumlah_depo <= 0:
            jumlah_depo = int(input("minimal memasukkan 1 koin: "))
        
        while jumlah_depo > koin:
            jumlah_depo = int(input(f"koin lu cuma {koin} kocakkk: "))
            
        koin -= jumlah_depo
            
        print(f'''
        Lihat kotak berikut:
        {'-'.join(kotak_kosong)}
        Pilih salah satu kotak untuk mendapatkan JAKPOTTT!![1/2/3/4]
        ''')
        
        pilihan = int(input("Masukkan pilihan mu: "))
        while pilihan < 1 or pilihan > 4:
            pilihan = int(input("Masukin angka yang bener lahh: "))
       
        if pilihan == jakpot:
                print(f"\nMantap kamu dapat JAKPOTTTTT\n{kotak}")
                koin += jumlah_depo * 2
        else:
                print(f"\nGa hokiiiiJAKPOTT ada di kotak {jakpot}\n{kotak}")
                      
        print(f"\nkoinmu sekarang {koin}")
        
        if koin <= 0 :
                print(" koinmu ga ada,Top up dulu dongg")
                main.main() 
    
        next = input("lanjut ga nihh?? [yes/no]: ")
        if next == "no":
            main.main()
            break
            
        

      
