import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


try:
    with psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM channels;")
            results = cursor.fetchall()
            for row in results:
                print(row)

except Exception as e:
    print("Error al conectar a la base de datos:", e)