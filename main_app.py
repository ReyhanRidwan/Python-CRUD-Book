import os 
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        
    print(f"{'Selamat Datang Di Program':^50}")
    print(f"{'Data Base Mahasiswa':^50}")
    print("\n")
    
    # check apakah database muncul
    CRUD.init_console()
    
while True:
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        
    print(f"{'Selamat Datang Di Program':^50}")
    print(f"{'Data Base Mahasiswa':^50}")
    print("\n")
        
        
    print("Pilih program: \t")
    print("1.Read Data")
    print("2.Create Data")
    print("3.Update Data")
    print("4.Delete Data")
        
    user_input = input("Masukan Pilihan(1-4): ")
        
    
    match user_input:
        case "1": CRUD.read_console()
        case "2": CRUD.create_console()
        case "3": CRUD.update_console()
        case "4": CRUD.delete_console()
        
    # apakah ingin keluar aplikasi
    is_done = input("Apakah ingin keluar aplikasi?(y/n)")
    if is_done == 'y':
        break