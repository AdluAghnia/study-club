def bio_data(nama, umur, prodi, uni):
    print(f"Nama = {nama}")
    print(f"Umur = {umur}")
    print(f"Prodi = {prodi}")
    print(f"Universitas = {uni}")

bio_data("Mamat", 19, "Sipil", "UMUS")


def hitung_umur(tahun_sekarang, tahun_lahir):
    umur = tahun_sekarang - tahun_lahir
    return umur

umur = hitung_umur(2024, 2003)
print(umur)
