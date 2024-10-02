
import main

def hitung():
    print("\n\nxxxx KALKULATOR PY xxxx")
    print("\n*note : untuk keluar ketik menu\n")
    
    while True:
        angka = input("Masukkan angka yang ingin di jumlahkan: ")
        
             
        if angka == "menu":    
            main.main()
            break
        
        else :
            hasil = eval(angka)
            print(f"Hasilnya adalah: {hasil}") 