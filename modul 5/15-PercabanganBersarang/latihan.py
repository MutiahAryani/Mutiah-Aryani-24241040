# Latihan
# data-data nilai

print(20*"=")
print("data nilai")
print(20*"=")

nilai = float(input("masukkan bilangan = "))
operator = input("operator (>, <=, >=)")

# data nilai percabangan

if operator == '<':
    hasil = nilai < 90
    print("hasil nilai huruf = A")
elif operator == '<=':
    hasil = nilai <= 90 and nilai >= 85
    print("hasil nilai huruf = A-")
elif operator == '<=':
    hasil = nilai <= 85 and nilai >= 80
    print("hasil nilai huruf = B+")
elif operator == '<=':
    hasil = nilai <= 79 and nilai >= 75
    print("hasil nilai huruf = B")
elif operator == '<=':
    hasil = nilai <= 74 and nilai >= 70
    print("hasil nilai huruf = B-")
elif operator == '<=':
    hasil = nilai <= 69 and nilai >= 65
    print("hasil nilai huruf = C+")
elif operator == '<=':
    hasil = nilai <= 64 and nilai >= 60
    print("hasil nilai huruf = C")
elif operator == '<=':
    hasil = nilai <= 59 and nilai >= 55
    print("hasil nilai huruf = D")
elif operator == '>':
    hasil = nilai > 69
    print("hasil nilai huruf = E")
print("terima kasih")