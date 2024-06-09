import psycopg2
from psycopg2 import sql

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=2+2equals-nein")
conn.autocommit = True

# Open a cursor to perform database operations
cur = conn.cursor()

# Create database named Paystack_Team
try:
    cur.execute("CREATE DATABASE Paystack_Team")
except psycopg2.Error as e:
    print(f"An error occurred while creating the database: {e}")
    cur.close()
    conn.close()
    exit(1)

# Close the initial connection
cur.close()
conn.close()

# Connect to the new database
try:
    conn = psycopg2.connect("dbname=Paystack_Team user=postgres password=2+2equals-nein")
except psycopg2.Error as e:
    print(f"An error occurred while connecting to the database: {e}")
    exit(1)

# Open a cursor to perform database operations
cur = conn.cursor()

# Create table for team members
cur.execute("""
CREATE TABLE team_members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    division VARCHAR(50),
    module INT
)
""")

# Define your queries here...

# Commit changes
conn.commit()

# Close communication with the database
cur.close()
conn.close()
