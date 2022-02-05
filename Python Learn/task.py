from traceback import print_tb


umur = 18
uang  = 125000

if umur >= 21 and uang >= 100000 :
    print("Boleh Masuk dan Bisa Beli Minum")
elif umur >= 21 and uang <= 100000 :
    print("Boleh Masuk, Tidak bisa beli minum")
else :
    print("Tidak Boleh Masuk")


umur = 20

while umur  < 20:
    print(umur ," Umur")
    umur = umur + 1

print(umur, "sudah menjadi lansia")

kupon = 10
while kupon > 0:
    print("You got 1 Ice Cream, Your Kupon Left", kupon)
    kupon -= 1
    if (kupon == 3):
        print("Too Many Attempt")
        break
print("Kupon Sisa", kupon)


