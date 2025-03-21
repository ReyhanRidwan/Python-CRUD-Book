from time import time
from . import Database
from .utils import random_string
import time

def delete(no_buku):
    try:
        with open(Database.DB_NAME, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Cek apakah no_buku valid
        if no_buku > len(lines) or no_buku < 1:
            print("Nomor buku tidak valid!")
            return False

        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            for i, line in enumerate(lines):
                if i != no_buku - 1:
                    file.write(line)
        
        print("Hapus berhasil!")
    except Exception as e:
        print(f"ERROR dalam hapus data: {e}")


def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, 'r', encoding="utf-8") as file:
            lines = file.readlines()

        # Cek apakah no_buku valid
        if no_buku > len(lines) or no_buku < 1:
            print("Nomor buku tidak valid!")
            return

        # Update baris yang sesuai
        lines[no_buku - 1] = data_str

        # Tulis ulang seluruh file
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.writelines(lines)

        print("Update berhasil!")
    except Exception as e:
        print(f"ERROR dalam update data: {e}")
        
def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah Gagal booooos")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            #jika ada parameter index maka akan memilih salah satu buku dan return salah satu buku
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:    
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    