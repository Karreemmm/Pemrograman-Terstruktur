print('------STATUS KELULUSAN MAHASISWA------')

# Input Nilai Ujian
print('\n')
BHSINDO = int(input('Masukkan nilai Bhs Indonesia : '))
IPA = int(input('Masukkan Nilai IPA : '))
MTK = int(input('Masukkan nilai Matematika : '))

# Menampilkan hasil
print('\n')
if (BHSINDO >= 60) and (IPA >= 60) and (MTK > 70):
    print('Status Kelulusan :' , 'LULUS')
else :
    print('Status Kelulusan :' , 'TIDAK LULUS')
