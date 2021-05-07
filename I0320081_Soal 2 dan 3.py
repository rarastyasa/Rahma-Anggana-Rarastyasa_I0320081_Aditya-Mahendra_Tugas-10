#Soal 2
##Membuat program biodata dengan menggunakan modul "w"

print ("########## Program Biodata Diri ##########")

nama_lengkap = input("Nama Lengkap: ")
nama_panggilan = input("Nama Panggilan: ")
umur = input("Umur: ")
hobi = input("Hobi: ")
pekerjaan = input("Pekerjaan: ")
alamat = input("Alamat: ")

teks = "Nama Lengkap: {}\nNama Panggilan: {}\nUmur: {}\nHobi: {}\nPekerjaan: {}\nAlamat: {}".format(nama_lengkap,nama_panggilan,umur,hobi,pekerjaan,alamat)

file_biodata = open("Biodata Diri.txt","w")

file_biodata.write(teks)

file_biodata.close()

#Soal 2
##Membuat program biodata dengan menggunakan modul "w"

print ("########## Program Biodata Diri ##########")

nama_lengkap = input("Nama Lengkap: ")
nama_panggilan = input("Nama Panggilan: ")
umur = input("Umur: ")
hobi = input("Hobi: ")
pekerjaan = input("Pekerjaan: ")
alamat = input("Alamat: ")

teks = "Nama Lengkap: {}\nNama Panggilan: {}\nUmur: {}\nHobi: {}\nPekerjaan: {}\nAlamat: {}".format(nama_lengkap,nama_panggilan,umur,hobi,pekerjaan,alamat)

file_biodata = open("Biodata Diri.txt","a")

file_biodata.write(teks)

file_biodata.close()

