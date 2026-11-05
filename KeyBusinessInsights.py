import pandas as pd

# Load data yang sudah dibersihkan dari langkah sebelumnya
cleaned_df = pd.read_csv('JC-202609-cleaned.csv')

# 1. Bandingkan Penggunaan: Member vs Casual
member_summary = cleaned_df.groupby('member_casual').agg(
    total_trips=('ride_id', 'count'),
    avg_duration_min=('duration_minutes', 'mean'),
    median_duration_min=('duration_minutes', 'median')
).reset_index()

print("--- Member vs Casual ---")
print(member_summary)

# 2. Jenis Sepeda Terfavorit
bike_summary = cleaned_df.groupby('rideable_type')['ride_id'].count().reset_index()
bike_summary.columns = ['rideable_type', 'total_trips']

print("\n--- Popularitas Sepeda ---")
print(bike_summary)

# 3. Top 5 Stasiun Awal Paling Sibuk
top_start_stations = cleaned_df['start_station_name'].value_counts().head(5)

print("\n--- Top 5 Stasiun Keberangkatan ---")
print(top_start_stations)