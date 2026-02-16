import pandas as pd
import requests

# Function to expand a shortened URL
def expand_url(url):
    response = requests.get(url, allow_redirects=False)
    if response.status_code in [301, 302]:
        return response.headers['Location']
    return url  # return the original URL if not expanded

# Read the spreadsheet containing URLs
input_file = 'urls.xlsx'
output_file = 'expanded_urls.xlsx'

# Assuming the URLs are in the first column (A) of the spreadsheet
# and the expanded URLs will be written to the second column (B)
try:
    df = pd.read_excel(input_file)
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        url = row[0]  # Access the first column (A)
        if pd.notna(url):  # Check if the cell is not blank
            expanded_url = expand_url(url)
            df.at[index, 1] = expanded_url  # Write to the second column (B)
    # Save the expanded URLs to a new spreadsheet
    df.to_excel(output_file, index=False)
    print('Expanded URLs saved successfully to', output_file)
except Exception as e:
    print('An error occurred:', e)