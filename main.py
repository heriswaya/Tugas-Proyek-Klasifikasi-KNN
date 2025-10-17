# Import modul kedua kita
import knn_functions

def run_app():
    # Loop utama program
    while True:
        print("\n--- Program Prediksi k-NN Sederhana ---")
        print("Masukkan data baru untuk diprediksi:")

        # KRITERIA: Error Handling dan Input User
        try:
            fitur1 = float(input("Masukkan Fitur 1 (berat badan (kg)): "))
            fitur2 = float(input("Masukkan Fitur 2 (tinggi badan (cm)): "))
            if fitur1 < 0 or fitur2 < 0:
                print("\nERROR: Fitur (berat/tinggi) tidak boleh negatif.")
                print("Silakan masukkan nilai yang valid.\n")
                continue
            if fitur1 > 75 or fitur2 > 150:
                print(f"\nPERINGATAN: Data {fitur1} atau {fitur2} di luar jangkauan wajar.")
                print("Hasil prediksi mungkin tidak akurat.")
        except ValueError:
            print("ERROR: Input harus berupa angka. Silakan coba lagi.")
            continue
        
        # KRITERIA: Dictionary (untuk data baru)
        data_baru = {'f1': fitur1, 'f2': fitur2}
        
        # Panggil fungsi dari modul dua untuk prediksi
        k = 3 # Saya memilih k = 3
        hasil_prediksi = knn_functions.prediksi_knn(data_baru, k)
        
        print(f"\n==> Hasil Prediksi: Label data baru adalah '{hasil_prediksi}'")
        
        # KRITERIA: Kondisional (if)
        tanya_lagi = input("Ingin prediksi lagi? (y/n): ")
        if tanya_lagi.lower() != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break

# Panggil fungsi utama
if __name__ == "__main__":
    run_app()