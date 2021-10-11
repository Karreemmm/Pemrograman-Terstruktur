# Waktu rental
jamMasuk = 6
menitMasuk = 0
jamKeluar = 23
menitKeluar = 50

# Biaya rental 12 jam pertama
biaya12Jam = 200000
 
# Biaya rental per 1 jam
biaya1Jam = 10000

# Selisih waktu rental
selisihJam = jamKeluar - jamMasuk
selisihMenit = menitKeluar - menitMasuk

# Total biaya rental
totalBiaya = biaya12Jam + biaya1Jam * (selisihJam -12)
totalBiaya = totalBiaya + biaya1Jam * (selisihMenit / 60)
totalBiaya = round(totalBiaya)

print ('Total waktu rental adalah', selisihJam, 'Jam', selisihMenit, 'Menit' )
print ('Total biaya rental adalah Rp', totalBiaya)
