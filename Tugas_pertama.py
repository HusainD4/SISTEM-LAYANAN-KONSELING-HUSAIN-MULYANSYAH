print("===="*16)
print( "\n===========   SELAMAT DATANG DI LAYANAN KONERLING   =========== \n")
print("===="*16)
nama = str (input('nama : ')); kelas =(input('kelas : ')); jurusan = {'1': "Teknik Informatika",'2': "Ilmu Komputer",'3': "Teknik Elektro",'4': "Teknik Mesin\n"}
print("Pilih jurusan yang Anda inginkan:")
for key, value in jurusan.items():
    print(f"{key}. {value}")
pilihan = input("Masukkan nomor jurusan yang Anda pilih: ")
if pilihan in jurusan:
    print(f"Anda memilih jurusan {jurusan[pilihan]}\n")
    laporan = (input('silakan ketik apa laporan anda : '))
    print("===="*16)
    hasil = (f'Terimakasih {nama}, {kelas}, jurusan {jurusan[pilihan]}, \nlaporan anda sudah kami terima! \ntetap semangat teruslah berusaha untuk masa depan yang cerah!'); print(hasil) ; print("===="*16)
else:
    print("Pilihan tidak valid. Silakan pilih nomor jurusan yang tersedia.")






