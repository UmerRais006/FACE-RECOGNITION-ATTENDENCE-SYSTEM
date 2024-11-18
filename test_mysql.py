'''import pymysql

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
        print("MySQL connection is closed")'''

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import os #for getting images
import cv2 #more than 2500+ algorithms
import numpy as np


import cv2

video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Unable to access the camera.")
else:
    print("Camera accessed successfully!")

while True:
    ret, frame = video_cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == 13:  # Press Enter to exit
        break

video_cap.release()
cv2.destroyAllWindows()
