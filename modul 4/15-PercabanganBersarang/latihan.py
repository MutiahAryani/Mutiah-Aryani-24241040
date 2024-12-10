# Fungsi untuk mengonversi nilai angka ke nilai huruf

if nilai > 90:
    return "A"
elif nilai >= 85 and nilai <= 90:  # Menggunakan operator logika AND
    return "A-"
elif nilai >= 80 and nilai < 85:
    return "B+"
elif nilai >= 75 and nilai < 80:
    return "B"
elif nilai >= 70 and nilai < 75:
    return "B-"
elif nilai >= 65 and nilai < 70:
    return "C+"
elif nilai >= 60 and nilai < 65:
    return "C"
elif nilai >= 55 and nilai < 60:
    return "D"
elif nilai < 55:  # Menggunakan operator komparasi <
    return "E"