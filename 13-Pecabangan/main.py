# percabangan
# struktur
"""
1. if -nya
2. punya kondisi
3. punya aksi
"""
nama = input("masukkan nama : ")

# percabangan yang inline (satu baris)
if nama == "adam" : print("selamat datang")
print("terima kasih")

# percabangan dengan indentasi
if nama == "adam" :
    print("selamat datang")
    print("selamat belajar python")
print("bukan bagian percabangan")

# percabangan 1 kondisi 2 aksi
# pakai kata kunci 'else'

if nama == "adam" :
    print(f"selamat datang {nama}")
else:
    print(f'anda {nama}, bukan adam' )
print("terima kasih")