CREATE WAREHOUSE dublin_transport_wh
WITH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED = TRUE;

CREATE DATABASE dublin_transport_db;

USE DATABASE dublin_transport_db;

CREATE SCHEMA luas;
CREATE SCHEMA dublin_bus;
CREATE SCHEMA weather;
CREATE SCHEMA dublin_bikes;
CREATE SCHEMA cycle_counts;

CREATE TABLE luas.passenger_counts (
    year INT NOT NULL,
    month STRING NOT NULL,
    line STRING NOT NULL,
    passengers INT NOT NULL,
    full_date DATE
);

CREATE TABLE dublin_bus.passenger_counts (
    year INT NOT NULL,
    month STRING NOT NULL,
    passengers INT NOT NULL,
    full_date DATE
);

CREATE TABLE weather.daily_observations (
    observation_date DATE NOT NULL,
    rain FLOAT,
    max_temp FLOAT,
    min_temp FLOAT,
    grass_min_temp FLOAT,
    soil_temp FLOAT,
    rain_indicator INT,
    max_temp_indicator INT,
    min_temp_indicator INT
);

CREATE TABLE dublin_bikes.station_data (
    last_reported TIMESTAMP NOT NULL,
    station_id INT NOT NULL,
    num_bikes_available INT NOT NULL,
    num_docks_available INT NOT NULL,
    is_installed BOOLEAN NOT NULL,
    is_renting BOOLEAN NOT NULL,
    is_returning BOOLEAN NOT NULL,
    station_name STRING NOT NULL,
    address STRING,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    capacity INT NOT NULL,
    last_reported_date DATE
);

CREATE TABLE cycle_counts.cycle_counts (
    timestamp TIMESTAMP NOT NULL,
    charleville_mall_total INT,
    charleville_mall_north INT,
    charleville_mall_south INT,
    clontarf_total INT,
    clontarf_west INT,
    clontarf_east INT,
    pebble_beach_total INT,
    pebble_beach_west INT,
    pebble_beach_east INT,
    drumcondra_inbound_total INT,
    drumcondra_inbound_west INT,
    drumcondra_inbound_east INT,
    drumcondra_outbound_total INT,
    drumcondra_outbound_east INT,
    drumcondra_outbound_west INT,
    griffith_clare_total INT,
    griffith_clare_south INT,
    griffith_clare_north INT,
    griffith_lane_total INT,
    griffith_lane_south INT,
    griffith_lane_north INT,
    grove_road_totem_total INT,
    grove_road_totem_out INT,
    grove_road_totem_in INT,
    north_strand_northbound INT,
    north_strand_southbound INT,
    richmond_inbound_total INT,
    richmond_inbound_south INT,
    richmond_inbound_north INT,
    richmond_outbound_total INT,
    richmond_outbound_north INT,
    richmond_outbound_south INT,
    date DATE
);