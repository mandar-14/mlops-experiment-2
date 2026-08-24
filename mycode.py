import os
import pandas as pd

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({
    "Name": ["Maddy", "John"],
    "Marks": [85, 90]
})

df.to_csv("data/students.csv", index=False)

print("CSV file created successfully!")