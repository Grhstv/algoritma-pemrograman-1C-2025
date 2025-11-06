def anagram(kata1, kata2):# Fungsi untuk memeriksa apakah dua kata adalah anagram
    return sorted(kata1) == sorted(kata2)# Mengurutkan kedua kata dan membandingkannya

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if anagram(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah ANAGRAM ")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram ")