import pandas as pd
import plotly.express as px

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Step 1: Group the data by 'organization_name' and count the number of prizes
org_grouped = df.groupby('organization_name').size().reset_index(name='total_prizes')

# Step 2: Create a Sunburst chart using Plotly
fig = px.sunburst(
    org_grouped,
    path=['organization_name'],  # Only one level in the hierarchy: organization name
    values='total_prizes',  # The size of each sector is determined by the number of prizes
    title='Sunburst Chart of Nobel Prizes by Organization',
    color='total_prizes',  # Use total prizes to color the sectors
    color_continuous_scale='Plasma'  # You can change this to any other color scale if needed
)

# Show the sunburst chart
fig.show()
