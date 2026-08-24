import os
import pandas as pd

os.makedirs("data", exist_ok=True)

file_path = "data/students.csv"

# Read existing data
df = pd.read_csv(file_path)

# Append a new row
new_row = pd.DataFrame({
    "Name": ["Rahul"],
    "Marks": [95]
})

df = pd.concat([df, new_row], ignore_index=True)

# Save updated data
df.to_csv(file_path, index=False)

print("New row appended successfully!")