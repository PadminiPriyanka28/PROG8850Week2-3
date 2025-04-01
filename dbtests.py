import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="subscribers"
)
cursor = conn.cursor()

# Check if the subscribers table exists with the new column
cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'subscription_date';")
result = cursor.fetchone()

if result:
    print("Test Passed: 'subscription_date' column exists.")
else:
    print("Test Failed: 'subscription_date' column is missing.")

conn.close()
