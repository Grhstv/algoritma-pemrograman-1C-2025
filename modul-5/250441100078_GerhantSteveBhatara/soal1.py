def faktorial(n):# Program menghitung faktorial secara rekursif memanggil fungsi dirinya sendiri
    if n == 0 or n == 1:# Basis: jika n == 0 atau n == 1, kembalikan 1
        return 1# Rekursi: n! = n * (n-1)!
    else:
        return n * faktorial(n - 1)# jika bukan 0/1, fungsi memanggil dirinya n-1 sampai kondisi dasar
angka = int(input("Masukkan bilangan bulat non-negatif: "))
print(f"Faktorial dari {angka} adalah: {faktorial(angka)}")