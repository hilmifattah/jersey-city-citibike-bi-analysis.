--script
CREATE TABLE trips (
    ride_id VARCHAR(50) PRIMARY KEY,
    rideable_type VARCHAR(30),
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    start_station_name VARCHAR(255),
    start_station_id VARCHAR(50),
    end_station_name VARCHAR(255),
    end_station_id VARCHAR(50),
    start_lat NUMERIC(10, 6),
    start_lng NUMERIC(10, 6),
    end_lat NUMERIC(10, 6),
    end_lng NUMERIC(10, 6),
    member_casual VARCHAR(20),
    duration_minutes NUMERIC(10, 2),
    start_hour INT,
    day_name VARCHAR(15),
    is_weekend INT
);

--query
--1. Analisis Jam Sibuk
SELECT 
    start_hour,
    COUNT(*) AS total_trips,
    ROUND(AVG(duration_minutes), 2) AS avg_duration
FROM trips
GROUP BY start_hour
ORDER BY total_trips DESC
LIMIT 5;

--2. Analisis Hari Kerja vs Akhir Pekan
SELECT 
    CASE WHEN is_weekend = 1 THEN 'Weekend' ELSE 'Weekday' END AS day_type,
    COUNT(*) AS total_trips,
    ROUND(AVG(duration_minutes), 2) AS avg_duration
FROM trips
GROUP BY is_weekend;

--3. Top 5 Rute Paling Populer
SELECT 
    start_station_name,
    end_station_name,
    COUNT(*) AS total_trips,
    ROUND(AVG(duration_minutes), 2) AS avg_duration
FROM trips
WHERE start_station_name IS NOT NULL AND end_station_name IS NOT NULL
GROUP BY start_station_name, end_station_name
ORDER BY total_trips DESC
LIMIT 5;

--4. Preferensi Jenis Sepeda Berdasarkan Tipe Pengguna
SELECT 
    member_casual,
    rideable_type,
    COUNT(*) AS total_trips,
    ROUND(AVG(duration_minutes), 2) AS avg_duration
FROM trips
GROUP BY member_casual, rideable_type
ORDER BY member_casual, total_trips DESC;