import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('vulnerable_database.db')
cursor = conn.cursor()

# Create a table in the database if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
''')
conn.commit()

# Streamlit app UI
st.title("Vulnerable User Management App")

# Function to fetch and display all data from the database
def display_data():
    query = "SELECT * FROM users"
    data = pd.read_sql_query(query, conn)
    st.write(data)

# Add a new user (Vulnerable to SQL Injection)
st.subheader("Add New User")
name = st.text_input("Name")
email = st.text_input("Email")
if st.button("Add User"):
    # Vulnerable query with direct user input
    cursor.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
    conn.commit()
    st.success("User added successfully")

# Delete user by ID (Vulnerable to SQL Injection)
st.subheader("Delete User")
user_id = st.text_input("Enter User ID to Delete")
if st.button("Delete User"):
    # Vulnerable query with direct user input
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    st.success("User deleted successfully")

# Update user by ID (Vulnerable to SQL Injection)
st.subheader("Update User Email")
update_id = st.text_input("Enter User ID to Update")
new_email = st.text_input("New Email")
if st.button("Update Email"):
    # Vulnerable query with direct user input
    cursor.execute(f"UPDATE users SET email = '{new_email}' WHERE id = {update_id}")
    conn.commit()
    st.success("User email updated successfully")

# Display data from the database
st.subheader("View All Users")
if st.button("Display Users"):
    display_data()

# Close the database connection when done
st.write("Close the database connection by clicking the 'End Session' button below.")
if st.button("End Session"):
    conn.close()
    st.info("Database connection closed")
