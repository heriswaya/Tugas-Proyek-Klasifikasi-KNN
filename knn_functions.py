import math

# KRITERIA: List dan Dictionary (sebagai data latih/dataset)
# Anggap datanya (f1=berat, f2=tinggi)
DATA_LATIH = [
    # --- Data Kucing (8 data) ---
    {'f1': 3.5, 'f2': 24, 'label': 'Kucing'},
    {'f1': 4.0, 'f2': 25, 'label': 'Kucing'},
    {'f1': 3.2, 'f2': 22, 'label': 'Kucing'},
    {'f1': 4.8, 'f2': 28, 'label': 'Kucing'},
    {'f1': 5.5, 'f2': 30, 'label': 'Kucing'},
    {'f1': 3.8, 'f2': 26, 'label': 'Kucing'},
    {'f1': 4.2, 'f2': 23, 'label': 'Kucing'},
    {'f1': 5.0, 'f2': 27, 'label': 'Kucing'},

    # --- Data Anjing (8 data) ---
    {'f1': 9.0, 'f2': 38, 'label': 'Anjing'},
    {'f1': 11.0, 'f2': 40, 'label': 'Anjing'},
    {'f1': 15.0, 'f2': 45, 'label': 'Anjing'},
    {'f1': 18.0, 'f2': 50, 'label': 'Anjing'},
    {'f1': 20.0, 'f2': 55, 'label': 'Anjing'},
    {'f1': 8.5, 'f2': 36, 'label': 'Anjing'},
    {'f1': 13.0, 'f2': 42, 'label': 'Anjing'},
    {'f1': 19.0, 'f2': 52, 'label': 'Anjing'},
]

# Fungsi untuk menghitung jarak (Euclidean Distance)
def hitung_jarak(data1, data2):
    jarak = math.sqrt((data1['f1'] - data2['f1'])**2 + (data1['f2'] - data2['f2'])**2)
    return jarak

# Fungsi utama untuk prediksi k-NN
def prediksi_knn(data_baru, k):
    list_jarak = []
    
    # KRITERIA: Looping (for)
    # 1. Hitung jarak dari data baru ke semua data latih
    for data in DATA_LATIH:
        jarak = hitung_jarak(data_baru, data)
        list_jarak.append( (jarak, data['label']) )
        
    # 2. Urutkan list berdasarkan jarak terpendek
    list_jarak.sort(key=lambda x: x[0])
    
    # 3. Ambil k tetangga terdekat
    tetangga_terdekat = list_jarak[:k] # Ambil 3 data teratas (karna tadi k=3)
    
    # 4. Lakukan voting untuk menentukan label
    # Pakai dictionary untuk menghitung suara
    suara = {}
    for jarak, label in tetangga_terdekat:
        suara[label] = suara.get(label, 0) + 1
        
    # Cari label dengan suara terbanyak
    hasil_voting = max(suara, key=suara.get)
    
    return hasil_voting