pilihan = "x"

while pilihan == "x" :
	print("=========================================================")
	print("|\t\t 	SEBLAK SEHATI			|")
	print("|\t\t 	 DAFTAR MENU			|")
	print("| 1. Seblak Ceker 				10000	|")
	print("| 2. Seblak Sosis				10000	|")
	print("| 3. Seblak Bakso				10000	|")
	print("| 4. Seblak Seafood				12000	|")
	print("| 5. Seblak Sosis+Bakso				12000	|")
	print("| 6. Seblak Sosis+Bakso+Mie			15000	|")
	print("| 7. Seblak Spesial				15000	|")
	print("| 8. Seblak Komplit				20000	|")
	print("| 9. Tidak memesan makanan				|")
	print("=========================================================")

	makanan = int(input("Mau Seblak Apa (Masukkan angka) = "))
	jumlah = int(input("Berapa porsi (Masukkan angka)? = "))


	if makanan == 1:
		harga = 10000*jumlah
	elif makanan== 2:
		harga = 10000*jumlah
	elif makanan == 3 : 
		harga = 10000*jumlah
	elif makanan == 4 : 
		harga = 12000*jumlah
	elif makanan == 5 : 
		harga = 12000*jumlah
	elif makanan == 6 : 
		harga = 15000*jumlah
	elif makanan == 7 : 
		harga = 15000*jumlah
	elif makanan == 8 : 
		harga = 20000*jumlah
	elif makanan == 9:
		break

	print("\t1. Es Jeruk\t\t7000")
	print("\t2. Es teh Manis\t\t5000")
	print("\t3. Air Putih\t\t3000")
	print("\t4. Teh Pucuk\t\t4000")
	print("\t5. Tidak memesan minuman")

	minum = int(input("Mau minum apa? = "))

	if minum == 1:
		jeruk=7000
		total= harga+jeruk
	elif minum == 2:
		esteh=5000
		total= harga+esteh
	elif minum == 3:
		air=3000
		total=harga+air
	elif minum == 4:
		pucuk=4000
		total=harga+pucuk
	elif minum == 5:
		pass

#Menghitung diskon
	if minum ==5:
		print("Total Pembayaran =",harga)
	elif jumlah > 5:
		diskon = harga - 3000
		print("Total Pembayaran =",diskon)
	elif jumlah < 5:
		print("Total Pembayaran =",total)
	break