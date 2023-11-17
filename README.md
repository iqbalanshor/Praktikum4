<H1>LATIHAN</H1>
<H2>1. Buat sebuah list sebanyak 5 elemen dengan nilai bebas</H2>
<p>list_elemen = [10, 'Python', 3.14, True, 'Data Sci</p>
<H2>2. Akses list :</H2>
A. Tampilkan elemen ke-3
<p>print("Elemen ke-3:", list_elemen[2])</p>
B. Ambil nilai elemen ke-2 sampai elemen ke-4
<p>nilai_elemen_2_4 = list_elemen[1:4]
print("Nilai elemen ke-2 sampai elemen ke-4:", nilai_elemen_2_4)</p>
C. Ambil elemen terakhir
<p>elemen_terakhir = list_elemen[-1]
print("Elemen terakhir:", elemen_terakhir)</p>
<H2>3. Ubah elemen list :</H2>
A. Ubah elemen ke-4 dengan nilai lainnya
<p>list_elemen[3] = False
print("List setelah mengubah elemen ke-4:", list_elemen)</p>
B. Ubah elemen ke-4 sampai dengan elemen terakhir
<p>list_elemen[3:] = [1, 2, 3]
print("List setelah mengubah elemen ke-4 sampai dengan elemen terakhir:", list_elemen)</p>
<H2>4. Tambah elemen list :</H2>
A. Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
<P>list_a = list_elemen[:2]
list_b = list_a.copy()</P>
B. Tambah list B dengan nilai string
<p>list_b.append('AI')</p>
C. Tambah list B dengan 3 nilai
<p>list_b.extend([7, 8, 9])</p>
D. Gabungkan list B dengan list A
<p>list_c = list_a + list_b
print("List setelah gabungkan list B dengan list A:", list_c)</p>
INI ADALAH TAMPILAN KODE PROGRAMNYA :

![gambar](screenshot/ss2.png)
INI ADALAH HASIL OUTPUTNYA :

![gambar](screenshot/outputss2.png)
<H1>PRAKTIKUM</H1>
# LIST
nama = []
nim = []
nilaiTugas = []
nilaiUTS = []
nilaiUAS = []
nilaiAkhir = []

print()

# Input
while True:
    nama.append(input("Masukan nama : "))
    nim.append(input("Masukan NIM  : "))
    Tugas = int(input("Nilai Tugas  : ")); 
    nilaiTugas.append(Tugas)
    UTS   = int(input("Nilai UTS    : ")); 
    nilaiUTS.append(UTS)
    UAS   = int(input("Nilai UAS    : ")); 
    nilaiUAS.append(UAS)

    nilaiAkhir.append(Tugas * 30/100 + UTS * 35/100 + UAS * 35/100)

    print()
    _tanya = input("Tambah data ? [y/t]: ")
    print()
    if(_tanya == "t"):
        break

# Output
print("+----+--------------------+-----------+--------+-------+-------+---------+")
print("| {0:^2} | {1:^18} | {2:^9} | {3:^6} | {4:^5} | {5:^5} | {6:^7} |".format("No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
print("-----+--------------------+-----------+--------+-------+-------+---------+")

no = 0
for nama, nim, Tugas, UTS, UAS, nilaiAkhir in zip(nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir):
    no += 1    
    print("| {0:>2} | {1:<18} | {2:>8} | {3:>6} | {4:>5} | {5:>5} | {6:>7} |".format(no, nama, nim, Tugas, UTS, UAS, nilaiAkhir))
print("+----+--------------------+-----------+--------+-------+-------+---------+")

INI ADALAH TAMPILAN KODE PROGRAMNYA :
![gambar](screenshot/ss1.png)
INI ADALAH HASIL OUTPUTNYA :
![gambar](screenshot/Outputss1.png)
