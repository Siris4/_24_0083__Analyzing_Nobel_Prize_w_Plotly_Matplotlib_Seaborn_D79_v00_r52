import pandas as pd
import plotly.express as px

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Step 1: Generate a Ranking of Birth Cities
birth_city_ranking = df.groupby('birth_city').size().reset_index(name='total_laureates')
birth_city_ranking = birth_city_ranking.sort_values(by='total_laureates', ascending=False)

# Step 2: Calculate the Total Number of Laureates
total_laureates = birth_city_ranking['total_laureates'].sum()

# Step 3: Calculate the Percentage for Each City
birth_city_ranking['percentage_of_total'] = (birth_city_ranking['total_laureates'] / total_laureates) * 100

# Step 4: Create a Plotly Bar Chart for the Top 20 Birth Cities, Including the Percentage
top_20_birth_cities = birth_city_ranking.head(20)

fig = px.bar(
    top_20_birth_cities,
    x='percentage_of_total',
    y='birth_city',
    orientation='h',
    title='Percentage of Nobel Laureates by Birth City (Top 20)',
    labels={'percentage_of_total': 'Percentage of Total Laureates (%)', 'birth_city': 'Birth City'},
    color='percentage_of_total',
    color_continuous_scale='Plasma'
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Percentage of Total Nobel Laureates (%)',
    yaxis_title='Birth City',
    yaxis=dict(autorange="reversed"),  # Reverse the y-axis to have the top city on top
    coloraxis_colorbar=dict(
        title="Percentage of Total Laureates"
    )
)

# Show the figure
fig.show()

# Display the DataFrame with percentages for verification
print(birth_city_ranking.head(20))
