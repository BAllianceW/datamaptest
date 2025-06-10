import pandas as pd

# Read the CSV file
df = pd.read_csv('2025 B1 Calls.csv')

# Get unique combinations of Initial Call Type and Priority
unique_calls = df[['Initial Call Type', 'Priority']].drop_duplicates()

# Sort by Initial Call Type and Priority
unique_calls = unique_calls.sort_values(['Initial Call Type', 'Priority'])

# Save to Excel file
unique_calls.to_excel('UniqueCallTypes.xlsx', index=False)

print("Processing complete! Unique call types and priorities have been saved to 'UniqueCallTypes.xlsx'") 