import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Ensure the birth date and prize year are in datetime format
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['prize_year'] = pd.to_numeric(df['year'], errors='coerce')

# Calculate the age when the laureate won the prize
df['age_at_prize'] = df['prize_year'] - df['birth_date'].dt.year

# Plot a histogram using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(df['age_at_prize'], bins=30, kde=True, color='skyblue')

# Add labels and title
plt.title('Distribution of Nobel Laureate Age at the Time of Winning', fontsize=16)
plt.xlabel('Age at Prize', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Adjust layout to avoid text cutoff
plt.tight_layout()

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\laureate_age_distribution.png"
plt.savefig(output_path)
