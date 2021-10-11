# Jarak yang ditempuh
jarakAB = 125
jarakBC = 256

# Rata-rata kecepatan
kecepatanAB = 62
kecepatanBC = 70

# Awal berangkat
jamBerangkat = 6
menitBerangkat = 00
menitIstirahat = 45 / 60

# Menghitung waktu tempuh 
waktuAB = round(jarakAB / kecepatanAB, 2)
waktuBC = round(jarakBC / kecepatanBC, 2)

totalWaktu = waktuAB + waktuBC + menitIstirahat
totalWaktu = round(totalWaktu, 2)

totalJam = totalWaktu // 1
jamSampai = totalJam + jamBerangkat

totalMenit = totalWaktu % 1
totalMenit = round(totalMenit * 60, 1)
menitSampai = round(totalMenit + menitBerangkat, 1)

# Menampilkan hasil
print("Waktu Tempuh dari Kota A ke B adalah", waktuAB, "Jam")
print("Waktu Tempuh dari Kota B ke C adalah", waktuBC, "Jam")
print("Total waktu perjalanan + istirahat 45 menit adalah", totalWaktu, "jam")
print("Atau", round(totalJam), "jam", round(totalMenit), "menit")
print("Jika berangkat pada pukul", jamBerangkat, "lebih", menitBerangkat)
print("Maka akan sampai pada pukul", round(jamSampai), "lebih", round(menitSampai))
