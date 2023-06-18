import pandas as pd

# Read the Excel file
df = pd.read_excel('Datasetl.xlsx')

# Strip leading and trailing white spaces from column names
df.columns = df.columns.str.strip()

# Get user input for location
location = input('Enter a location: ')

# Clean the input location by stripping leading/trailing whitespaces
location = location.strip()

# Filter the data based on the location and availability
filtered_data = df[(df['Location'].str.strip() == location) & (df['Availability'].str.strip().eq('Available'))]

# Print the filtered data
if filtered_data.empty:
    print('No vehicles available at this location.')
else:
    filtered_data = filtered_data[['Location', 'Driver Name', 'Vehicle Type', 'Timestamp', 'Availability']]
    display(filtered_data)
