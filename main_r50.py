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

# Create a Seaborn regplot with a trendline
plt.figure(figsize=(12, 6))
sns.regplot(data=df, x='prize_year', y='age_at_prize', ci=None, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

# Add labels and title
plt.title('Trend of Nobel Laureate Age at Time of Award Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Age at Prize', fontsize=14)

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_regplot.png"
plt.savefig(output_path)
