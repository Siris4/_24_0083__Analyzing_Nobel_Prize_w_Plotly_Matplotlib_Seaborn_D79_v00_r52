import pandas as pd
import plotly.express as px

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Step 1: Group the data by 'birth_country_current', 'birth_city', and 'organization_name' and count occurrences
df_grouped = df.groupby(['birth_country_current', 'birth_city', 'organization_name']).size().reset_index(name='prize_count')

# Step 2: Create a Sunburst chart using Plotly
fig = px.sunburst(
    df_grouped,
    path=['birth_country_current', 'birth_city', 'organization_name'],  # Define the hierarchy
    values='prize_count',  # The size of each sector is determined by the count of prizes
    title='Sunburst Chart of Nobel Prizes by Country, City, and Organization',
    color='prize_count',  # Use the count of prizes to color the sectors
    color_continuous_scale='Plasma'  # Use the 'Plasma' color scale
)

# Update layout for a better appearance
fig.update_layout(margin=dict(t=30, l=0, r=0, b=0))

# Show the sunburst chart
fig.show()
