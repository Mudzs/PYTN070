import imp
import importlib
from traceback import print_tb


def sapa():
    print("Halo")

sapa()


def sapaNama(siapa):
    print("Halo", siapa)
    print("Halo Ganteng Selamat Kembali")

sapaNama("Jihad")

def siapaNamaWaktu(siapa, waktu):
    print("Halo", siapa)
    print("Jam", waktu)

siapaNamaWaktu("Jihad", 12)

# Untuk data yang tipe simple (int, float, bool, str) akan selalu di pass by. sedangkan yang lebih structured:
# (list, tuple, dictionary) aka selalu di pass by refrence

rumah = ["jakarta", 'indonesia']
kopi_rumah = rumah
kopi_rumah[0] = 'bangka'
print(rumah)

# harus hati hati dengan data yang structured karen bisa merubah data asli
# pass by yang asli adalah saat data yang asli tidak berubah

rumah = 'jakarta, indonesia'
kopi_rumah = rumah

kopi_rumah = 'bangka, indonesia'
print(rumah)

# Nambah Function

list_buah = ['apel', 'pir', 'semangka']
def nambahBuah(lb, buah):
    lb.append(buah)
    print(lb)

nambahBuah(list_buah, "kelapa")
print(list_buah)

# Diubah Function 
def nambahBuah(lb, buah):
    copy_list = lb.copy()
    copy_list.append(buah)
    print(copy_list)
nambahBuah(list_buah, "Jeruk")

print(list_buah)

# Required argument
def contoh(argi):
    print("ini function contoh")

# Tidak bisa di run karena argi masih kosong

# contoh cara mengisi argumen dengan keywoard

# function menyapa menggunakan nama orang, waktu , dan tempat
def sapa2(nama, tempat, waktu):
    print("selamat", tempat, waktu)
    print("selamat datang di", tempat)
    return

sapa2("Nub", "pagi", "yes")

sapa2(waktu="12", nama="Jihad", tempat="bandung")

# Mengisi dengan Keyword waktu=

# default argument Tidak harus di isi karena otomatis terisi

def sapa2(nama='pak', tempat='bandung', waktu='siang'):
    print("selamat", waktu, nama)
    print("selamat datang di", tempat)

sapa2()

# variable leght argument

def namaBanyak(waktu, *orang):
    for o in orang:
        print("Selamat", waktu, o)

namaBanyak("malam")
namaBanyak("malam", "kamis", "hartini")

def hitung(panjang, lebar):
    return panjang * lebar
    print("bro") # tidak bisa karena print sudah di dahului return

hitungan = hitung(12,12)
print = hitungan
# return menghetikan function

# function tidak print melainkan melihatkan data lepas terakhir
def yes(sm):
    return
ah = yes('q')

# Jangan gunakan global var di dalam function
import lesson3mdl
lesson3mdl.nama1

#Kita bisa import karena file berada di folder sama
# Modul bisa cari dimana saja dengan command sys

import sys
sys.path

# kita bisa tambahin sendiri

import lesson2
importlib.reload(lesson2)

from lesson2 import nilai as nilaiTugas

# Kita tidak bisa import pkg 
# Kita tidak bisa akses module mod didalam pkg

#cara benar









