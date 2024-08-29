import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Ensure the birth date and prize year are in datetime format
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['prize_year'] = pd.to_numeric(df['year'], errors='coerce')

# Calculate the age when the laureate won the prize
df['age_at_prize'] = df['prize_year'] - df['birth_date'].dt.year

# Calculate descriptive statistics for 'age_at_prize'
count = df['age_at_prize'].count()
mean = df['age_at_prize'].mean()
std_dev = df['age_at_prize'].std()
min_age = df['age_at_prize'].min()
percentile_25 = df['age_at_prize'].quantile(0.25)
median = df['age_at_prize'].median()
percentile_75 = df['age_at_prize'].quantile(0.75)
max_age = df['age_at_prize'].max()

# Display the results
print(f"Descriptive Statistics for Nobel Laureates' Age at the Time of Award:")
print(f"Count: {count}")
print(f"Mean: {mean:.2f} years")
print(f"Standard Deviation: {std_dev:.2f} years")
print(f"Minimum Age: {min_age} years")
print(f"25th Percentile (25% are younger than): {percentile_25} years")
print(f"Median (50% are younger than): {median} years")
print(f"75th Percentile (75% are younger than): {percentile_75} years")
print(f"Maximum Age: {max_age} years")
