#LIST KOSONG DIISI KEMUDIAN
nim = []
nama = []
alamat = []
asalsekolah = []
kodeprodi = []
ipkawal = []
uts = []
uas = []
tm = []
nilaiips = []
ipkakhir = []
beasiswa = []


#INPUT DENGAN LOOPING JUMLAH YANG DIINGINKAN
x = int(input('Masukkan Jumlah Data Mahasiswa yang diinginkan : '))
for z in range(1,x+1):
    a = int(input('Masukkan NIM : '))
    b = input('Masukkan Nama : ')
    c = input('Masukkan Alamat : ')
    d = input('Masukkan Asal Sekolah : ') 
    e = input('Masukkan Kode Prodi : ')
    f = int(input('Masukkan Nilai IPK Awal : '))
    g = int(input('Masukkan Nilai UTS : '))
    h = int(input('Masukkan Nilai UAS : '))
    i = int(input('Masukkan Nilai TM : '))
    j = (g*0.3) + (h*0.4) + (i*0.3)
    k = (f+h)/2

    #PERHITUNGAN BEASISWA
    if e == 'TI' and k > 75 and k < 85:
        bea = 'Beasiswa 20%'
    elif e == 'TI' and k > 85 and k < 100:
        bea = 'Beasiswa 30%'
    elif e == 'SI' and k > 75 and k < 85:
        bea = 'Beasiswa 20%'
    elif e == 'SI' and k > 85 and k < 100:
        bea = 'Beasiswa 30%'
    elif e == 'DKV' and k > 75 and k < 85:
        bea = 'Beasiswa 25%'
    elif e == 'DKV' and k > 85 and k < 100:
        bea = 'Beasiswa 35%'
    elif e == 'Teknik Industri' and k > 75 and k < 85:
        bea = 'Beasiswa 25%'
    elif e == 'Teknik Industri' and k > 85 and k < 100:
        bea = 'Beasiswa 35%'
    else :
        bea = 'Beasiswa 0%'
    
        
    #APPEND LIST DARI INPUT 
    nim.append(a)
    nama.append(b)
    alamat.append(c)
    asalsekolah.append(d)
    kodeprodi.append(e)
    ipkawal.append(f)
    uts.append(g)
    uas.append(h)
    tm.append(i)
    nilaiips.append(j)
    ipkakhir.append(k)
    beasiswa.append(bea)
    nestedList = nim,nama,alamat,asalsekolah,kodeprodi,ipkawal,uts,uas,tm,nilaiips,ipkakhir,beasiswa

#TRANSPOSE LIST PER VARIABLE MENJADI PER NIM
print('NIM          | Nama         | Alamat       | Asal Sekolah | Kode Prodi   | IPK Awal     | Nilai UTS    | Nilai UAS    | Nilai TM     | IPS          | IPK Akhir    | Beasiswa     |')
for v in range(x):
    for w in range(len(nestedList)):
        print(nestedList[w][v], end=' '*(13-len(str(nestedList[w][v]))) + '| ')
    print()