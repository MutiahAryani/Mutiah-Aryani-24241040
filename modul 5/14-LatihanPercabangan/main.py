# Input total belanja
total_belanja = int(input("Masukkan total belanja Anda: "))

# Logika penentuan hadiah
if total_belanja > 500000:
    hadiah = "mouse dan keyboard"
else:
    hadiah = "gantungan kunci"

# Output hasil
print(f"Total belanja Anda: Rp{total_belanja:,}")
print(f"Anda mendapatkan hadiah: {hadiah}")