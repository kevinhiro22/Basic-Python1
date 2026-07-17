'''
    =================================================
    Graded Challenge 2

    Nama  : Hiro Kevin Rudyanto
    Batch : CODA-RMT-018

    Program ini dibuat untuk melakukan automatisasi agar user bisa menambah, menghapus, melihat barang, dan juga melihat total harga belanjanya di keranjang belanja (cart) mereka.
    =================================================
    '''
#ini adalah variable untuk menyimpan data barang menggunakan list of dictionary.
shopping_cart = [] # [ {'nama':'apel','harga':2400}, {'nama' : 'jeruk', 'harga':3000} ]

def tambah_cart():

    nama = input('Masukan nama barang:')
    harga = int(input('Masukan harga:')) #casting ke int dari string

    item = {'nama':nama, 'harga':harga} #dictionary
    shopping_cart.append(item) #masukkan item dictionary ke dalam list

    print("Barang", nama," berhasil dimasukkan ke keranjang.")

'''
fungsi ini ditujukan untuk menginput barang ke dalam shopping cart pembelian user.
'''


def hapus_cart() :

    nama = input('Masukan nama barang yang ingin dihapus:')

    for item in shopping_cart:
        if item['nama'] == nama: 
            
            shopping_cart.remove(item)
            print('Barang',nama, 'berhasil dihapus di keranjang belanja.')
            break

'''
fungsi ini ditujukan untuk menghapus barang dari shopping cart yang sudah diisi oleh user
'''


def lihat_cart():
    print('Barang di Keranjang:')
    
    for i, item in enumerate(shopping_cart):
        #print(i,item)
        print(f"{i}. {item["nama"]} - Rp {item["harga"]}")
        #print(i,". ",item["nama"], " - ")

'''
fungsi ini ditujukan untuk user agar bisa melihat barang apa saja yang sudah ditambahkan ke shopping cart.
'''


def total_cart():
    total = 0
    for item in shopping_cart:
        total = total + item['harga']
    print('Total Belanja: Rp ', total)

'''
fungsi ini ditujukan untuk user agar bisa melihat total harga belanja dari barang yang sudah dimasukkan ke shopping cart.
'''

'''fungsi while dibawah ini ditujukan agar sistem aplikasi dapat digunakan berulang kali oleh user.'''
while True:
    print('menu')
    print('1.Menambahkan Barang')
    print('2.Hapus Barang')
    print('3.Tampilkan Barang di Keranjang')
    print('4.Lihat Total Belanja')
    print('5.Exit')
    menu=input('pilih menu:')

    if menu =='1':
        tambah_cart()
    elif menu =='2':
        hapus_cart()
    elif menu =='3':
        lihat_cart()
    elif menu =='4':
        total_cart()
    elif menu =='5':
        print('Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.')
        break
    else:
        print('Pilihannya salah. Coba lagi ya.')

'''
fungsi if diatas ditujukan untuk mengatur alur menu dalam aplikasi agar dapat membaca pilihan user yang disimpan dalam variabel menu, kemudian menjalankan fungsi sesuai dengan pilihan yang user pilih 
'''