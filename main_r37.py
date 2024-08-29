import pandas as pd

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# List of European countries (you may need to customize this list)
european_countries = [
    'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
    'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
    'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
    'Malta', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania',
    'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'United Kingdom'
]

# Filter the data to only include rows where the birth country is in Europe
european_data = df[df['birth_country_current'].isin(european_countries)]

# Group by 'birth_city' (or 'organization_city' if relevant) and count the total number of prizes
total_prizes_by_city = european_data.groupby('birth_city').size().reset_index(name='total_prizes')

# Sort by the total number of prizes won in descending order
sorted_cities = total_prizes_by_city.sort_values(by='total_prizes', ascending=False)

# Display the city with the most discoveries
most_discoveries_city = sorted_cities.head(1)
print(most_discoveries_city)
