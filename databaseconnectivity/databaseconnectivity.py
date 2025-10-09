import psycopg2

try:
    # Establish connection
    conn = psycopg2.connect(
        host="localhost",
        database="chonduDB",
        user="postgres",
        password="admin1234"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Insert data
    cur.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
                ('Alice', 20, 'Computer Science'))
    conn.commit()
    print("Record inserted successfully.")

    # Retrieve data
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    print("\n🎓 Student Records:")
    for row in rows:
        print(row)

    # Update data
    cur.execute("UPDATE students SET age = %s WHERE name = %s", (21, 'Alice'))
    conn.commit()
    print("\n Record updated successfully.")

    # Delete data

except Exception as e:
    print(" Error:", e)

finally:
    if conn:
        cur.close()
        conn.close()
        print("\n Database connection closed.")
