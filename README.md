# portalurlvalidation
This script processes an Excel file containing ArcGIS Portal content inventory, appends a valid URL prefix to the content IDs, checks the validity of URLs

This script to be ran after running the GIS Enterprise Reporter tool. The purpose of this script is verify the URLs in the portal inventory are actually working. If they dont run, then its best to make note of the URLS and reach out to the creators to verify. 

Make sure you get the spreadsheet with the gis_portal_content from the GIS enterprise reporter results. You will need to insert that parameter in the python script. 

### GIS Portal Content URL Validator Script

**Description**:  
This script processes an Excel file containing ArcGIS Portal content inventory, appends a valid URL prefix to the content IDs, checks the validity of URLs, and marks whether each URL is valid or not. It reads an Excel file, filters the content, checks if the URLs are functional, and saves the results to a new Excel file with a "Validity" column added.

**Features**:
- Reads a portal content inventory from an Excel file.
- Adds a URL prefix to the item `id` field to create valid URLs for ArcGIS Portal items.
- Checks the validity of each URL by sending a GET request and marking whether the URL is working or not.
- Saves the processed data into a new Excel file with a "Validity" column.

**Usage**:
1. **Update Credentials**: Replace `'your_username'` and `'your_password'` in the script with valid credentials, or use a secure method for storing them.
2. **File Paths**: Update the file paths for both input (`file_path`) and output (`output_file_path`) Excel files.
3. **Portal URL**: Replace the placeholder `https://your-gis-portal-url` with the actual URL of your ArcGIS portal.

**Example**:
```python
file_path = "/path/to/your/file/gis_state_portal_content.xlsx"
output_file_path = "/path/to/your/file/filtered_gis_urls.xlsx"
```

**Requirements**:
- Python 3.x
- `pandas` and `requests` libraries

**Installation**:
You can install the required Python libraries using:
```bash
pip install pandas requests
```

**Notes**:
- The script assumes that the Excel file has an 'id' column containing item IDs and a 'url' column with URLs to be checked.
- Ensure you have proper access to the portal and permissions to access the content.

---
