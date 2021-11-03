#Mengambil input
nama_lengkap = input("Nama lengkap : ")
nama_panggilan = input("Nama panggilan : ")
npm = input("Npm : ")
umur = input("Umur : ")
tempat_lahir = input("Tempat lahir : ")
telepon = input("Telepon : ")
alamat = input("Alamat : ")


print("="*149)
print("="*149)

txt = "Assalamu'alaikum.\n\nLet me introduce my self. My name is {}, but you can call me {}. My NPM is {}. I was born in {} and I am {} years old. I am very glad if you want to invite my house in {}. So, don't forget to call me before with the number {}.\n\nThank you."

#Menampilkan output
print(txt.format(nama_lengkap, nama_panggilan,npm, tempat_lahir, umur, alamat, telepon))

print("="*149) 
print("="*149)
