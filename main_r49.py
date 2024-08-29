import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Ensure the birth date and prize year are in datetime format
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['prize_year'] = pd.to_numeric(df['year'], errors='coerce')

# Calculate the age when the laureate won the prize
df['age_at_prize'] = df['prize_year'] - df['birth_date'].dt.year

# Group by year and calculate the average age for each year
avg_age_per_year = df.groupby('prize_year')['age_at_prize'].mean().reset_index()

# Plot the trend of average ages over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=avg_age_per_year, x='prize_year', y='age_at_prize', marker='o')

# Add labels and title
plt.title('Average Age of Nobel Laureates at the Time of Award Over Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Age', fontsize=14)

# Show the plot
plt.tight_layout()

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\avg_age_over_years.png"
plt.savefig(output_path)
