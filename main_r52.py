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

# Set up the figure for plotting
g = sns.FacetGrid(df, col="category", col_wrap=2, height=4, aspect=1.5)

# Apply sns.regplot to each subplot
g.map(sns.regplot, 'prize_year', 'age_at_prize', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

# Add a title to the entire figure
g.fig.suptitle('Trend of Nobel Laureate Age at Time of Award by Category', fontsize=16)
g.fig.subplots_adjust(top=0.9)  # Adjust subplots to fit the title

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_lmplot_by_category.png"
g.savefig(output_path)
