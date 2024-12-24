# menghitung tinggi badan (dalam cm) dan berat badan (dalam kg)
tinggi_badan = float(input("masukkan tinggi badan anda (cm) :"))
berat_badan = float(input("masukkan berat badan (kg) :"))

# menghitung BMI (tinggi badan diubah ke meter)
tinggi_badan_m = tinggi_badan / 100
BMI = berat_badan / (tinggi_badan_m ** 2)

# menampilkan skor BMI dengan format string
print (f"skor BMI anda adalah : {BMI :.if}")