# Program menghitung total belanja dengan diskon

# Input dari pengguna
member = input("Apakah Member? (ya/tidak): ").strip().lower()
total_belanja = int(input("Masukkan total belanja (dalam Rp): "))

# Inisialisasi variabel diskon
diskon_persen = 0

# Logika pemberian diskon
if member == "ya":
    if total_belanja > 500_000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:  # Jika bukan member
    if total_belanja > 500_000:
        diskon_persen = 5

# Hitung nilai diskon dan total bayar
diskon = (diskon_persen / 100) * total_belanja
total_bayar = total_belanja - diskon

# Output hasil
print("\nOutput:")
print(f"Total belanja : Rp {total_belanja:,.0f}")
print(f"Diskon persen : {diskon_persen}%")
print(f"Diskon        : Rp {diskon:,.0f}")
print(f"Bayar         : Rp {total_bayar:,.0f}")