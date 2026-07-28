import psycopg2 
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
from extract import extract_logs
from transform import transform_logs

load_dotenv()

KEY_TRANSACTION =  "id_transaction"
KEY_TIMESTAMP = "timestamp"
KEY_CHANNEL = "channel"
KEY_OPERATION = "operation_type"
KEY_RESPONSE_CODE = "response_code"
KEY_AMOUNT = "amount"
KEY_LATENCY = "latency_ms"

def obtain_values (data_transform: list[dict]) -> list[tuple]:
    data = []

    for i in range (len(data_transform)):
        transaction_id = data_transform[i][KEY_TRANSACTION]
        timestamp = data_transform[i][KEY_TIMESTAMP]
        channel_id = data_transform[i][KEY_CHANNEL]
        operation_type = data_transform[i][KEY_OPERATION]
        code_id = data_transform[i][KEY_RESPONSE_CODE]
        amount = data_transform[i][KEY_AMOUNT]
        latency_ms = data_transform[i][KEY_LATENCY]
        temp_data = (transaction_id,channel_id,code_id,latency_ms,amount,timestamp,operation_type)
        data.append(temp_data)


    return data

def load_logs(data_transform : list[dict]):

    sql = "INSERT INTO transactions(transaction_id,channel_id,code_id,latency_ms,amount,timestamp,operation_type) VALUES %s"

    data = obtain_values(data_transform)

    try:    
        with psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            ) as connection :
            with connection.cursor() as cursor : 
                execute_values(cursor,
                               sql,
                               data
                                )
    except psycopg2.Error as e:
        print("Hubo problemas con la base de datos", e)



if __name__ == "__main__":
    extract_data = extract_logs("logs_example.json")
    transform_data = transform_logs(extract_data)
    load_logs(transform_data)
    
