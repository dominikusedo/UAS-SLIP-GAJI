# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:17:36 2021

@author: DOMINIKUS EDO KRISTIAN - 20083000121
"""
import datetime
x = datetime.datetime.now()

print("=======================================")
print("          SLIP GAJI CV.LOGOS           ")
print("---------------------------------------")
print("          Tanggal : " + (x.strftime("%x")))
print("=======================================")

nm = input("Masukkan Nama = ")

gol = input("Masukkan Golongan (1/2/3) = ")
if int(gol)==1:
    gjpok = 2500000
elif int(gol)==2:
    gjpok = 4500000
elif int(gol)==3:
    gjpok = 6500000

gen = input("Masukkan Jenis Kelamin (1.Laki-laki 2.Perempuan) = ")
if int(gen)==1:
    nmgen = "Laki-laki"
elif int(gen)==2:
    nmgen = "Perempuan"

sts = input("Masukkan Status Kawin (1.Kawin 2.Belum Kawin) = ")
if int(sts)==1:
    nmsts = "Kawin"
elif int(sts)==2:
    nmsts = "Belum Kawin"

if int(gen)==1 and int(sts)==1:
    if int(gol)==1:
        tunis = 0.01*gjpok
    elif int(gol)==2:
        tunis = 0.03*gjpok
    elif int(gol)==3:
        tunis = 0.05*gjpok
else:
    tunis = 0

if int(sts)==1:
    anak = input("Sudah punya anak ? (1.Sudah 2.Belum) = ")
    if int(anak)==1:
        tunan = 0.02*gjpok
    else:
        tunan = 0
else:
    tunan = 0
    
gjbrut = gjpok + tunan + tunis
byjab = 0.05*gjbrut
iurpen = 15500
iurorg = 3500
gjnet = gjbrut - byjab - iurpen - iurorg

print("")
print("=======================================")
print("          SLIP GAJI CV.LOGOS           ")
print("---------------------------------------")
print("          Tanggal : " + (x.strftime("%x")))
print("=======================================")
print("Nama             = " + nm)
print("Golongan         = " + gol)
print("Jenis Kelamin    = " + nmgen)
print("Status Kawin     = " + nmsts)
print("Gaji Pokok       = Rp. " + format(gjpok,",.2f"))
print("Tunjangan Istri  = Rp. " + format(tunis,",.2f"))
print("Tunjangan Anak   = Rp. " + format(tunan,",.2f"))
print(">> Gaji Bruto    = Rp. " + format(gjbrut,",.2f"))
print("Biaya Jabatan    = Rp. " + format(byjab,",.2f"))
print("Iuran Pensiun    = Rp. " + format(iurpen,",.2f"))
print("Iuran Organisasi = Rp. " + format(iurorg,",.2f"))
print(">> Gaji Netto    = Rp. " + format(gjnet,",.2f"))
print("=======================================")