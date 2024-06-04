import uppercase_counter

text1 = "Ini Adalah Contoh Teks"
text2 = "SEMUA HURUF BESAR"
text3 = "semua huruf kecil"

print(f"Jumlah huruf besar dalam '{text1}': {uppercase_counter.count_uppercase(text1)}")
print(f"Jumlah huruf besar dalam '{text2}': {uppercase_counter.count_uppercase(text2)}")
print(f"Jumlah huruf besar dalam '{text3}': {uppercase_counter.count_uppercase(text3)}")