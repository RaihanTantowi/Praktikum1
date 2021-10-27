print("hello")
print("Saya sedang belajar python")

a = 8
b = 6
print("variable a = ", a)
print("variable b = ", b)
print("Hasil penjumlahan a+b = ", a+b)

a = input("masukan nilai a : ")
b = input("masukan nilai b : ")

#a = int(input("masukan nilai a : "))
#b = int(input("masukan nilai b : "))
print("variable a = ", a)
print("variable b = ", b)
print("Hasil penggabungan {0}&{1}=%s".format(a, b) % (a+b))

# konversi nilai variable
a = int(a)
b = int(b)
print("hasil penjumlahan {0}+{1}=%d".format(a, b) % (a+b))
print("hasil pembagian {0}/{1}=%f".format(a, b) % (a/b))
