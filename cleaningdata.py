import pandas as pd

# 1. Load Data
df = pd.read_csv('JC-202609-citibike-tripdata.csv')

# 2. Konversi Kolom Waktu ke Format Datetime
df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

# 3. Hitung Durasi Perjalanan (dalam Menit)
df['duration_minutes'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60

# 4. Filter Anomali Data
# - Hapus baris yang kehilangan koordinat akhir (end_lat / end_lng)
# - Buang perjalanan < 1 menit (karena biasanya cuma salah lepas/pasang dock)
cleaned_df = df.dropna(subset=['end_lat', 'end_lng']).copy()
cleaned_df = cleaned_df[cleaned_df['duration_minutes'] >= 1]

# 5. Ekstrak Fitur Waktu Tambahan (Penting buat Analisis)
cleaned_df['start_hour'] = cleaned_df['started_at'].dt.hour
cleaned_df['day_name'] = cleaned_df['started_at'].dt.day_name()
cleaned_df['is_weekend'] = cleaned_df['started_at'].dt.dayofweek.isin([5, 6]).astype(int)

# 6. Cek Ringkasan Data Hasil Cleaning
print(f"Jumlah baris awal  : {len(df)}")
print(f"Jumlah baris bersih: {len(cleaned_df)}")
print(cleaned_df[['duration_minutes', 'start_hour']].describe())

# 7. Simpan File yang Sudah Clean
cleaned_df.to_csv('JC-202609-cleaned.csv', index=False)