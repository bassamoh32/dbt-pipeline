from api_request import mock_fetch_data
import psycopg2 


def connect_db():
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        print(conn)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise


def create_table(conn):
    print("Creating weather_data table if it does not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed INT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT now(),
                utc_offset FLOAT
            );
        """)
        conn.commit()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        conn.rollback()
        raise





def insert_records(conn, data):
    print("Inserting records into the database...")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, time, inserted_at, utc_offset)
            VALUES (%s, %s, %s, %s, %s, NOW(),%s);
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset'] 
            ))
        conn.commit()
        print("Records inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting records: {e}")
        raise

def  main():
    try:
        data = mock_fetch_data()
        conn = connect_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")    
    finally:
        if "conn" in locals():
            conn.close()
            print("Database connection closed.")

main()