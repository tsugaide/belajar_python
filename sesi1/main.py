
from welcome import welcome_message,stop
from program import cuypy_maxwin
from program import kalkulator
from program import warung_mini

def menu():
    option= int(input("Daftar Program\n1.CUYPy Maxwin\n2.Kalkulator\n3.Warung mini\n4.exit program\n\nPilih program yang ingin di janlankan: "))
    if option == 1:
        cuypy_maxwin.start()
    elif option == 2:
        kalkulator.hitung()
    elif option == 3:
        warung_mini.start()
    elif option == 4:
        stop()

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()
    

    
    

    

