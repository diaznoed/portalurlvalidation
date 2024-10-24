import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# Function to check URL validity
def is_valid_url(url):
    try:
        response = requests.get(url, auth=HTTPBasicAuth('your_username', 'your_password'))  # <--- Update with your credentials
        return response.status_code == 200
    except Exception as e:
        print("Error checking URL:", e)
        return False

# Read the Excel file containing portal content inventory
file_path = "/path/to/your/file/gis_state_portal_content.xlsx"  # <--- Update with your file path
sheet_name = "Inventory"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Add prefix to the 'id' column to form full URLs
df['id'] = 'https://your-gis-portal-url/portal/home/item.html?id=' + df['id'].astype(str)  # <--- Update with your portal URL

# Keep only necessary columns: 'id', 'url', 'modified', 'numViews', 'title'
df = df[['id', 'url', 'modified', 'numViews', 'title']]

# Drop rows where 'url' is missing (NaN)
df.dropna(subset=['url'], inplace=True)

# Save the filtered data to a new Excel file
output_file_path = "/path/to/your/file/filtered_gis_urls.xlsx"  # <--- Update with your output file path
df.to_excel(output_file_path, index=False)

print("Filtered data saved to:", output_file_path)

# Read the filtered Excel file
df_filtered = pd.read_excel(output_file_path)

# Check URL validity and update the 'Validity' column
validity = []
for index, row in df_filtered.iterrows():
    url = row['url']
    if is_valid_url(url):
        validity.append("Valid")
    else:
        validity.append("Not Working")

# Add the 'Validity' column to the DataFrame
df_filtered['Validity'] = validity

# Save the updated DataFrame back to the Excel file
df_filtered.to_excel(output_file_path, index=False)

print("Validity status added to the file:", output_file_path)
