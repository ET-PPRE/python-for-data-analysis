# Panel output data
panel_output = {
    'Panel1': [23, 25, 28, 21, 26, 27, 25],        # [kWh]
    'Panel2': [24, -9999, 27, 26, -88888, 29, 26], # [kWh]
    'Panel3': [20, 22, 23, 21, 24, 25, 22]         # [kWh]
}

# Cleaned version with negative values replaced by 0
panel_output_cleaned = panel_output
for panel, values in panel_output_cleaned.items():
    for i, v in enumerate(values):
        if v < 0:
            values[i] = 0

# Function for total weekly energy production
def weekly_production(week_data):
    return sum(week_data)

# Print each panel’s label and weekly total
# Find the panel with the highest total output
most_produced = ""
max_weekly = 0
print("Weekly production per panel:")
for panel, data in panel_output_cleaned.items():
    total = weekly_production(data)
    if total > max_weekly:
        max_weekly = total
        most_produced = panel
    print(f"{panel}: {total} kWh")

# Print the panel with the highest total output
print()
print("Panel with the highest output:", most_produced)