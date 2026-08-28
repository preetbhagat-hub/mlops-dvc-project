import os
import pandas as pd

os.makedirs("data", exist_ok=True)

data = {
    "Name": ["Preet", "Rahul", "Aman"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_csv("data/students.csv", index=False)

print("CSV file created successfully!")
