import pandas as pd
import sqlite3

print("Starting ETL Pipeline...")

# ======================
# STEP 1: EXTRACT
# ======================
df = pd.read_csv("logs.txt")
print("Data Loaded:\n", df)

# ======================
# STEP 2: TRANSFORM
# ======================
df['cpu_usage'] = df['cpu_usage'].astype(int)

# Create new column (important for interviews)
df['status_flag'] = df['status'].apply(lambda x: 1 if x == "FAIL" else 0)

print("\nTransformed Data:\n", df)

# ======================
# STEP 3: LOAD
# ======================    
conn = sqlite3.connect("network_data.db")
df.to_sql("logs", conn, if_exists="replace", index=False)

print("\nData stored in database successfully!")
cursor = conn.cursor()

print("\nFailure Count:")
for row in cursor.execute("""
SELECT device, COUNT(*) 
FROM logs 
WHERE status = 'FAIL' 
GROUP BY device
"""):
    print(row)