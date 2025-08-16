import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
# --- 1. Synthetic Data Generation ---
# Set seed for reproducibility
np.random.seed(42)
random.seed(42)
# Number of deliveries
num_deliveries = 1000
# Generate synthetic data
data = {
    'Delivery_ID': range(1, num_deliveries + 1),
    'Date': [datetime.date(2024, random.randint(1, 12), random.randint(1, 28)) for _ in range(num_deliveries)],
    'Origin_Latitude': [random.uniform(34, 35) for _ in range(num_deliveries)],
    'Origin_Longitude': [random.uniform(-118, -117) for _ in range(num_deliveries)],
    'Destination_Latitude': [random.uniform(34, 35) for _ in range(num_deliveries)],
    'Destination_Longitude': [random.uniform(-118, -117) for _ in range(num_deliveries)],
    'Distance_km': np.random.uniform(5, 30, size=num_deliveries),
    'Delivery_Time_minutes': np.random.uniform(15, 120, size=num_deliveries),
    'Traffic_Delay_minutes': np.random.poisson(lam=5, size=num_deliveries), #Simulate Poisson distributed traffic delays
    'Weather_Delay_minutes': np.random.poisson(lam=2, size=num_deliveries), #Simulate Poisson distributed weather delays
    'Cost_per_km': np.random.uniform(1, 3, size=num_deliveries) #Cost varies per delivery
}
df = pd.DataFrame(data)
df['Total_Cost'] = df['Distance_km'] * df['Cost_per_km']
df['Total_Delivery_Time'] = df['Delivery_Time_minutes'] + df['Traffic_Delay_minutes'] + df['Weather_Delay_minutes']
# --- 2. Analysis ---
# Calculate total delivery costs
total_cost = df['Total_Cost'].sum()
print(f"Total Delivery Cost: ${total_cost:.2f}")
# Calculate average delivery time
avg_delivery_time = df['Total_Delivery_Time'].mean()
print(f"Average Delivery Time: {avg_delivery_time:.2f} minutes")
#Analyze impact of delays on cost
df['Delay_Impact_Cost'] = (df['Traffic_Delay_minutes'] + df['Weather_Delay_minutes']) * df['Cost_per_km']
avg_delay_impact = df['Delay_Impact_Cost'].mean()
print(f"Average Cost Increase due to Delays: ${avg_delay_impact:.2f}")
# --- 3. Visualization ---
plt.figure(figsize=(10, 6))
plt.hist(df['Total_Delivery_Time'], bins=20)
plt.title('Distribution of Total Delivery Time')
plt.xlabel('Total Delivery Time (minutes)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
output_filename = 'delivery_time_distribution.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
plt.figure(figsize=(10,6))
plt.scatter(df['Distance_km'], df['Total_Cost'])
plt.title('Total Cost vs. Distance')
plt.xlabel('Distance (km)')
plt.ylabel('Total Cost ($)')
plt.grid(True)
plt.tight_layout()
output_filename2 = 'cost_vs_distance.png'
plt.savefig(output_filename2)
print(f"Plot saved to {output_filename2}")