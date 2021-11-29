nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('='*52)
print('NIM'.ljust(8),'NAMA'.ljust(16),'N.MID'.ljust(8),'N.UAS')
print('-'*52)
for i in nilai:
    print(i['nim'].ljust(8),i['nama'].upper().ljust(18),str(i['mid']).ljust(8),str(i['uas']))
print('='*52)
