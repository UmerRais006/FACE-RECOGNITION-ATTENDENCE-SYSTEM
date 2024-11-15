import pymysql

try:
    # Replace these values with your MySQL server details
    connection = pymysql.connect(
        host="localhost",        # MySQL server address (e.g., localhost)
        user="root",             # MySQL username
        password="newpasswordnew",  # MySQL password
        database="face_recognizer"  # MySQL database name
    )

    print("Successfully connected to MySQL database")

    # Example query to check connection
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in database:", tables)

except pymysql.MySQLError as err:
    print(f"Error occurred: {err}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("MySQL connection is closed")
