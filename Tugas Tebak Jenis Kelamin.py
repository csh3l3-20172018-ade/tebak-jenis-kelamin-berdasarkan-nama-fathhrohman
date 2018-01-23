#Masukkan nama seseorang
x = input("Masukkan nama : ")
#Mengubah dari nama tadi yang awalnya string menjadi char dalam list
y = list(x)
#mencari nama pertama
#variable awal adalah penanda apakan dia termasuk nama pertama
awal = True
nama_awal = []
for i in y :
    #Jika variable awal true dan i bukan ' ' maka dia akan dimasukkan kedalam list nama_awal
    if i == ' ':
        awal = False
    elif awal == True and i != ' ' :
        nama_awal.append(i)
#kita sudah mendapatkan nama awalnya sekarang mencari jenis kelaminnya
#untuk mencari jenis kelaminnya akan digunakan variable jk yang akan menentukan apakah dia laki-laki atau perempuat
jk = 0
for i in nama_awal :
    #jika i adalah huruf i,a,u,e,t,l maka akan cenderung ke perempuan
    #jika i adalah huruf b,d,o maka akan cenderung ke laki laki
    if i == 'i' or i == 'a' or i == 'u' or i == 'e' or i == 't' or i == 'l' :
        jk = jk - 1
    elif i == 'b' or i == 'd' or i == 'o' :
        jk = jk + 1
if (jk < 0) :
    print ("Jenis kelamin perempuan")
elif (jk > 0 ):
    print ("Jenis kelamin laki-laki")
else :
    print ("Jenis kelamin tidak diketahui")

#data sampel laki - laki : fathur rohman , kamal hasan , victor leadero
#hasil : perempuan, perempuan, perempuan
#data sampe perempuan : chlaudiah julinar , vina effendi , septiana putri , dhia imtinan
#hasil : perempuan, perempuan, perempuan, perempuan
#hasilnya hampir selalu perempuan karena lebih banyak huruf untuk perempuan sedangkan laki-lakinya sulit untuk keluar