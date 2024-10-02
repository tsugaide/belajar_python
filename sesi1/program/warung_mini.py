import main
from service import db

def add():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = int(input("Masukkan harga barang: "))
    stok_barang = int(input("Masukkan stok barang: "))
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
    
def check():
    rows = db.fetch_item()
    
    for row in rows:
        no = row[0]
        kode_barang = row[1]
        nama_barang = row[2]
        harga_barang = row[3]
        stok_barang = row[4]
        
        print(f"\n{no}. Kode barang: {kode_barang}\nNama barang: {nama_barang} || Rp{harga_barang}\nStok: {stok_barang}")

def start():
    while True:
        option = int(input("\nDaftar Menu:\n1. Tambah Barang\n2. Check barang\n3. Keluar\n\nPilih menu yang ingin dilakukan: "))
        
        if option == 1:
            add()
        elif option == 2:
            check()
        elif option == 3:
            main.main()
            break
        
if __name__ == '__main__':
    start()