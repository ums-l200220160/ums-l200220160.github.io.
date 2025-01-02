class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.spp_terbayar = False
        self.mata_kuliah = []
        self.nilai = {}

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_terbayar = True
        print("SPP berhasil dibayar!")

    def daftar_mata_kuliah(self):
        if not self.spp_terbayar:
            print("Anda harus membayar SPP terlebih dahulu.")
            return

        print("Daftar mata kuliah tersedia:")
        daftar = ["Algoritma", "Struktur Data", "Basis Data", "Pemrograman Web"]
        for i, mk in enumerate(daftar, start=1):
            print(f"{i}. {mk}")

        pilihan = input("Masukkan nomor mata kuliah yang ingin diambil (pisahkan dengan koma): ")
        pilihan = pilihan.split(",")
        for p in pilihan:
            try:
                index = int(p.strip()) - 1
                if 0 <= index < len(daftar):
                    self.mata_kuliah.append(daftar[index])
                    self.nilai[daftar[index]] = None
            except ValueError:
                print(f"Input tidak valid: {p}")

        print("Mata kuliah yang berhasil didaftarkan:", self.mata_kuliah)

    def mengikuti_perkuliahan(self):
        if not self.mata_kuliah:
            print("Anda belum mendaftar mata kuliah.")
            return

        print("Proses perkuliahan sedang berlangsung...")
        for mk in self.mata_kuliah:
            print(f"Mengikuti perkuliahan {mk}...")

    def isi_nilai(self):
        if not self.mata_kuliah:
            print("Anda belum mendaftar mata kuliah.")
            return

        print("Masukkan nilai akhir untuk setiap mata kuliah:")
        for mk in self.mata_kuliah:
            while True:
                try:
                    nilai = float(input(f"Nilai untuk {mk}: "))
                    if 0 <= nilai <= 100:
                        self.nilai[mk] = nilai
                        break
                    else:
                        print("Nilai harus antara 0-100.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")

    def tampilkan_hasil(self):
        print("\nHasil Akhir:")
        for mk, nilai in self.nilai.items():
            print(f"{mk}: {nilai}")

# Main Program
print("Selamat datang di simulasi kuliah Informatika!")
nama = input("Masukkan nama Anda: ")
npm = input("Masukkan NPM Anda: ")

mahasiswa = Mahasiswa(nama, npm)
mahasiswa.bayar_spp()
mahasiswa.daftar_mata_kuliah()
mahasiswa.mengikuti_perkuliahan()
mahasiswa.isi_nilai()
mahasiswa.tampilkan_hasil()
