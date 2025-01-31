import pandas as pd

# Load the Excel file
file_path = 'cycle_counts.xlsx'  # Update this to your file path
df = pd.read_excel(file_path)

# Replace blank cells with actual NULL values
df = df.where(df.notna(), None)

# Simplify column names
column_mappings = {
    "Time": "timestamp",
    "Charleville Mall (Unable to Reinstall Repaired Counter due to Roadworks 23.08.2023)": "charleville_mall_total",
    "Charleville Mall (Unable to Reinstall Repaired Counter due to Roadworks 23.08.2023) North Cyclist": "charleville_mall_north",
    "Charleville Mall (Unable to Reinstall Repaired Counter due to Roadworks 23.08.2023) South Cyclist": "charleville_mall_south",
    "Clontarf - James Larkin Rd": "clontarf_total",
    "Clontarf - James Larkin Rd Cyclist West": "clontarf_west",
    "Clontarf - James Larkin Rd Cyclist East": "clontarf_east",
    "Clontarf - Pebble Beach Carpark": "pebble_beach_total",
    "Clontarf - Pebble Beach Carpark Cyclist West": "pebble_beach_west",
    "Clontarf - Pebble Beach Carpark Cyclist East": "pebble_beach_east",
    "Drumcondra Cyclists Inbound (Not On Site - Roadworks) Cyclist": "drumcondra_inbound_total",
    "Drumcondra Cyclists Inbound (Not On Site - Roadworks) Cyclist West": "drumcondra_inbound_west",
    "Drumcondra Cyclists Inbound (Not On Site - Roadworks) Cyclist East": "drumcondra_inbound_east",
    "Drumcondra Cyclists Outbound (Not On Site - Roadworks)": "drumcondra_outbound_total",
    "Drumcondra Cyclists Outbound (Not On Site - Roadworks) Cyclist East": "drumcondra_outbound_east",
    "Drumcondra Cyclists Outbound (Not On Site - Roadworks) Cyclist West": "drumcondra_outbound_west",
    "Griffith Avenue (Clare Rd Side)": "griffith_clare_total",
    "Griffith Avenue (Clare Rd Side) Cyclist South": "griffith_clare_south",
    "Griffith Avenue (Clare Rd Side) Cyclist North": "griffith_clare_north",
    "Griffith Avenue (Lane Side)": "griffith_lane_total",
    "Griffith Avenue (Lane Side) Cyclist South": "griffith_lane_south",
    "Griffith Avenue (Lane Side) Cyclist North": "griffith_lane_north",
    "Grove Road Totem": "grove_road_totem_total",
    "Grove Road Totem OUT": "grove_road_totem_out",
    "Grove Road Totem IN": "grove_road_totem_in",
    "North Strand Rd N/B (Counter Removed for Roadworks) Cyclist": "north_strand_northbound",
    "North Strand Rd S/B (Counter Removed for Roadworks) Cyclist": "north_strand_southbound",
    "Richmond Street Inbound": "richmond_inbound_total",
    "Richmond Street Inbound Cyclist South": "richmond_inbound_south",
    "Richmond Street Inbound Cyclist North": "richmond_inbound_north",
    "Richmond Street Outbound": "richmond_outbound_total",
    "Richmond Street Outbound Cyclist North": "richmond_outbound_north",
    "Richmond Street Outbound Cyclist South": "richmond_outbound_south"
}

# Rename columns
df.rename(columns=column_mappings, inplace=True)

# Save the processed data to a CSV file without "NULL" as text
output_csv = 'processed_cycle_counts.csv'
df.to_csv(output_csv, index=False)

print(f"Processed data saved to {output_csv}")