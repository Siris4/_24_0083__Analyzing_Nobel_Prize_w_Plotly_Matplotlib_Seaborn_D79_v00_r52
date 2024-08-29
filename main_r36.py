import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file from the specified location
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by 'organization_name' and count the total number of prizes won by each organization
total_prizes_by_organization = df.groupby('organization_name').size().reset_index(name='total_prizes')

# Sort by the total number of prizes won in descending order
sorted_organizations = total_prizes_by_organization.sort_values(by='total_prizes', ascending=False).head(20)

# Set a color palette using Seaborn
colors = sns.color_palette('muted', len(sorted_organizations))

# Plot a horizontal bar chart with customized colors
plt.figure(figsize=(12, 8))
plt.barh(sorted_organizations['organization_name'],
         sorted_organizations['total_prizes'],
         color=colors)

# Add labels and title
plt.xlabel('Total Number of Prizes Won', fontsize=14)
plt.ylabel('Organization Name', fontsize=14)
plt.title('Top 20 Organizations by Total Number of Nobel Prizes Won', fontsize=16)
plt.gca().invert_yaxis()  # Invert y-axis to show the highest values at the top

# Adjust layout to avoid text cutoff
plt.tight_layout(pad=3.0)

# Save the plot as an image file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\top20_organizations_by_total_prizes.png"
plt.savefig(output_path)

# No need for plt.show() since we're saving the file
