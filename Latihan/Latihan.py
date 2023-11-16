# Buat list dengan 5 elemen dan nilai bebas
list_elemen = [10, 'Python', 3.14, True, 'Data Science']

# Akses list
# Tampilkan elemen ke-3
print("Elemen ke-3:", list_elemen[2])

# Ambil nilai elemen ke-2 sampai elemen ke-4
nilai_elemen_2_4 = list_elemen[1:4]
print("Nilai elemen ke-2 sampai elemen ke-4:", nilai_elemen_2_4)

# Ambil elemen terakhir
elemen_terakhir = list_elemen[-1]
print("Elemen terakhir:", elemen_terakhir)

# Ubah elemen list
# Ubah elemen ke-4 dengan nilai lainnya
list_elemen[3] = False
print("List setelah mengubah elemen ke-4:", list_elemen)

# Ubah elemen ke-4 sampai dengan elemen terakhir
list_elemen[3:] = [1, 2, 3]
print("List setelah mengubah elemen ke-4 sampai dengan elemen terakhir:", list_elemen)

# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
list_a = list_elemen[:2]
list_b = list_a.copy()

# Tambah list B dengan nilai string
list_b.append('AI')

# Tambah list B dengan 3 nilai
list_b.extend([7, 8, 9])

# Gabungkan list B dengan list A
list_c = list_a + list_b
print("List setelah gabungkan list B dengan list A:", list_c)