import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Ensure the birth date and prize year are in datetime format
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['prize_year'] = pd.to_numeric(df['year'], errors='coerce')

# Calculate the age when the laureate won the prize
df['age_at_prize'] = df['prize_year'] - df['birth_date'].dt.year

# Find the youngest laureate
youngest_laureate = df.loc[df['age_at_prize'].idxmin()]

# Find the oldest laureate
oldest_laureate = df.loc[df['age_at_prize'].idxmax()]

# Display the results
print("Youngest Laureate:")
print(youngest_laureate[['full_name', 'birth_date', 'prize_year', 'age_at_prize']])

print("\nOldest Laureate:")
print(oldest_laureate[['full_name', 'birth_date', 'prize_year', 'age_at_prize']])
