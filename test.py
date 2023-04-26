import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='house_sales')

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Execute the SHOW TABLES query
cursor.execute("Select * from bike where house_id=1")

# Fetch all the tables from the result set
tables = cursor.fetchall()

# Print the names of all the tables
for table in tables:
    print(table)

# Close the cursor and connection
cursor.close()
cnx.close()