import pandas as pd

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Step 1: Generate a Ranking of Birth Cities
# Group by 'birth_city' and count the total number of laureates born in each city
birth_city_ranking = df.groupby('birth_city').size().reset_index(name='total_laureates')
birth_city_ranking = birth_city_ranking.sort_values(by='total_laureates', ascending=False)

# Display the top 10 birth cities
print("Top 10 Birth Cities:")
print(birth_city_ranking.head(10))

# Step 2: Generate a Ranking of Discovery Cities (using 'organization_city')
# Group by 'organization_city' and count the total number of discoveries made in each city
discovery_city_ranking = df.groupby('organization_city').size().reset_index(name='total_discoveries')
discovery_city_ranking = discovery_city_ranking.sort_values(by='total_discoveries', ascending=False)

# Display the top 10 discovery cities
print("\nTop 10 Discovery Cities (Organization Cities):")
print(discovery_city_ranking.head(10))

# Step 3: Compare the Rankings
# Let's see if there are common cities in both lists
common_cities = pd.merge(birth_city_ranking.head(10), discovery_city_ranking.head(10), left_on='birth_city', right_on='organization_city', how='inner')

print("\nCommon Cities in Both Rankings:")
print(common_cities)
