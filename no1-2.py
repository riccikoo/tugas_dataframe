#"Dengan menggunakan pustaka pandas di Python, 
# buatlah sebuah DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat. 
# Pastikan kolom-kolomnya menyertakan nama Kabupaten/Kota, jumlah produksi sampah (dalam ton), dan tahun pencatatan."

import pandas as pd

data_sampah = pd.read_csv('data.csv')[['nama_kabupaten_kota','jumlah_produksi_sampah', 'tahun']]

# "Dari DataFrame yang telah dibuat, hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu. 
# Tampilkan hasilnya."
while True:
    try:
        thn = int(input("Masukkan tahun : "))
        total = 0
        status = 0

        for i, row in data_sampah.iterrows():
            if row['tahun'] == thn:
                status = 1
                total += row['jumlah_produksi_sampah']

        if status == 1:
            print(f"Total sampah di Jawa Barat pada tahun {thn}: {total} ton")
            data_sampah = pd.DataFrame({
                'tahun': [thn],
                'total_sampah': [total]
            })
            filename_csv = f'total_sampah({thn}).csv'
            filename_excel = f'total_sampah({thn}).xlsx'
            data_sampah.to_csv(filename_csv, index=False)
            data_sampah.to_excel(filename_excel, index=False, sheet_name='Data Sampah')
            print(f"Data berhasil disimpan ke file {filename_csv} dan {filename_excel}")
        else:
            print(f"Data tidak ditemukan untuk tahun {thn}")
    except ValueError:
        print("Input tidak sesuai, masukkan angka tahun yang valid.")

    pilihan = input("Apakah Anda ingin melanjutkan? (yes/no): ").strip().lower()
    if pilihan == 'no':
        print("Terimakasih")
        break
    elif pilihan != 'yes':
        print("Pilihan tidak valid. Program akan dilanjutkan.")
