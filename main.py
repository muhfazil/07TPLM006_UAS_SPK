'''
Author : Mochammad Ihza Rizky Karim
'''

from googletrans import Translator

# Detect Languages (Deteksi Bahasa)

# buat variabel bahasa untuk inputan kata atau kalimat
bahasa = input("Masukkan Kalimat atau Kata : ")

# selanjutnya, buat variabel translator untuk memanggil fungsi translator
translator = Translator()

# buat variabel deteksi yang didalamnya untuk memanggil variabel translator 
# fungsi detect yang menyimpan parameter bahasa untuk mendeteksi bahasa yang diinputkan
deteksi = translator.detect(bahasa)

print("Bahasa : ",deteksi)