import pandas as pd

data_sampah = pd.read_csv('data.csv')[['nama_kabupaten_kota','jumlah_produksi_sampah', 'tahun']]

total = data_sampah.groupby(['tahun', 'nama_kabupaten_kota'])['jumlah_produksi_sampah'].sum().reset_index()
total.rename(columns={'jumlah_produksi_sampah': 'total_sampah'}, inplace=True)

print("Total sampah per kota/kabupaten per tahun:")
for i, j in enumerate(total.itertuples(index=False), start=1):
    print(f"{i}. Tahun: {j.tahun}, Kota/Kabupaten: {j.nama_kabupaten_kota}, Total Sampah: {j.total_sampah} ton")

filename_csv = 'total_sampah_kota_per_tahun.csv'
filename_excel = 'total_sampah_kota_per_tahun.xlsx'
total.to_csv(filename_csv, index=False)
total.to_excel(filename_excel, index=False, sheet_name='Data Sampah')
print(f"Data berhasil disimpan ke file {filename_csv} dan {filename_excel}")
