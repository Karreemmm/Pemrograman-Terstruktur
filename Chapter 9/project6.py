nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('='*72)
print('NIM'.ljust(8),'NAMA'.ljust(16),'N.MID'.ljust(8),'N.UAS'.ljust(8),'N.AKHIR'.ljust(16),'STATUS')
print('-'*72)
for i in nilai:
    nilaiAkhir = round((i['mid'] + 2*i['uas'])/3,2)
    if (nilaiAkhir>=60):
        status= 'LULUS'
    else :
        status = 'TIDAK LULUS'
    print(i['nim'].ljust(8),i['nama'].upper().ljust(16),str(i['mid']).ljust(8),str(i['uas']).ljust(8),str(nilaiAkhir).ljust(16),status)
print('='*72)
