print('------STATUS KELULUSAN MAHASISWA------')

# Input Nilai Ujian
print('\n')
BHSINDO = int(input('Masukkan nilai Bhs Indonesia : '))
IPA = int(input('Masukkan Nilai IPA : '))
MTK = int(input('Masukkan nilai Matematika : '))

# Menampilkan hasil
print('\n')
if (BHSINDO > 100) or (IPA > 100) or (MTK > 100)or (BHSINDO < 0) or (IPA < 0) or (MTK < 0):
    print('Maaf input ada yang tidak valid')
elif (BHSINDO >= 60) and (IPA >= 60) and (MTK > 70):
    print('Status Kelulusan :' , 'LULUS')
else :
    print('Status Kelulusan :' , 'TIDAK LULUS')
  
