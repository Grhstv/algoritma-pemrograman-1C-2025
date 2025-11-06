def hitung_gaji(nama, jabatan, gaji_pokok):# Fungsi untuk menghitung gaji bersih karyawan
    pajak = 0.05 * gaji_pokok# Pajak sebesar 5% dari gaji pokok

    if jabatan.lower() == "manager":# Tunjangan untuk manager adalah 10% dari gaji pokok
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":# Tunjangan untuk staff adalah 5% dari gaji pokok
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0 

    gaji_bersih = gaji_pokok - pajak + tunjangan# Menghitung total gaji bersih

  
    print(f"Nama Karyawan  : {nama}")
    print(f"Jabatan        : {jabatan}")
    print(f"Gaji Pokok     : Rp {gaji_pokok:.0f}")
    print(f"Tunjangan      : Rp {tunjangan:.0f}")
    print(f"Pajak (5%)     : Rp {pajak:.0f}")
    print(f"Gaji Bersih    : Rp {gaji_bersih:.0f}")

nama = input("Masukkan nama karyawan: ")# Meminta input dari pengguna
jabatan = input("Masukkan jabatan (Manager/Staff): ")# Meminta input dari pengguna
gaji_pokok = float(input("Masukkan gaji pokok: "))# Meminta input dari pengguna

hitung_gaji(nama, jabatan, gaji_pokok)# Memanggil fungsi untuk menghitung gaji bersih 