import pandas as pd
import plotly.express as px

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Step 1: Generate a Ranking of Birth Cities
# Group by 'birth_city' and count the total number of laureates born in each city
birth_city_ranking = df.groupby('birth_city').size().reset_index(name='total_laureates')
birth_city_ranking = birth_city_ranking.sort_values(by='total_laureates', ascending=False)

# Step 2: Create a Plotly Bar Chart for the Top 20 Birth Cities
top_20_birth_cities = birth_city_ranking.head(20)

fig = px.bar(
    top_20_birth_cities,
    x='total_laureates',
    y='birth_city',
    orientation='h',
    title='Top 20 Birth Cities of Nobel Laureates',
    labels={'total_laureates': 'Total Laureates', 'birth_city': 'Birth City'},
    color='total_laureates',
    color_continuous_scale='Plasma'
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Total Number of Laureates',
    yaxis_title='Birth City',
    yaxis=dict(autorange="reversed"),  # Reverse the y-axis to have the top city on top
    coloraxis_colorbar=dict(
        title="Number of Laureates"
    )
)

# Show the figure
fig.show()
