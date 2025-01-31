ALTER TABLE luas.passenger_counts ADD COLUMN full_date DATE;

UPDATE luas.passenger_counts
SET full_date = CASE
    WHEN month = '-' THEN NULL
    ELSE date_from_parts(year, TRY_CAST(month AS INT), 1)
END;

ALTER TABLE dublin_bus.passenger_counts ADD COLUMN full_date DATE;

UPDATE dublin_bus.passenger_counts
SET full_date = CASE
    WHEN month = '-' THEN NULL
    ELSE date_from_parts(year, TRY_CAST(month AS INT), 1)
END;

ALTER TABLE dublin_bikes.station_data ADD COLUMN last_reported_date DATE;

UPDATE dublin_bikes.station_data
SET last_reported_date = CAST(last_reported as DATE);

ALTER TABLE cycle_counts.cycle_counts ADD COLUMN date DATE;

UPDATE cycle_counts.cycle_counts
SET date = CAST(timestamp as DATE);