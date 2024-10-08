print("Pilih Operasi (+, -, *, /)")

operasi = input("Operasi : ")

angka_1 = float(input("angka 1 : "))
angka_2 = float(input("angka 2 : "))

if operasi == "+":
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
elif operasi == "-":
    hasil = angka_1 - angka_2
    print(f"{angka_1} - {angka_2} = {hasil}")
elif operasi == "*":
    hasil = angka_1 * angka_2
    print(f"{angka_1} * {angka_2} = {hasil}")
elif operasi == "/":
    hasil = angka_1 / angka_2
    print(f"{angka_1} / {angka_2} = {hasil}")
else:
    print("INPUT INVALID")
