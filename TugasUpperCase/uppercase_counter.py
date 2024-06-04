def count_uppercase(text):
    """
    Menghitung jumlah huruf besar (Upper Case) dalam sebuah teks.

    Args:
        text (str): Teks yang akan dihitung jumlah huruf besarnya.

    Returns:
        int: Jumlah huruf besar dalam teks.
    """
    uppercase_count = sum(1 for char in text if char.isupper())
    return uppercase_count
import uppercase_counter

text1 = "Ini Adalah Contoh Teks"
text2 = "SEMUA HURUF BESAR"
text3 = "semua huruf kecil"

print(f"Jumlah huruf besar dalam '{text1}': {uppercase_counter.count_uppercase(text1)}")
print(f"Jumlah huruf besar dalam '{text2}': {uppercase_counter.count_uppercase(text2)}")
print(f"Jumlah huruf besar dalam '{text3}': {uppercase_counter.count_uppercase(text3)}")