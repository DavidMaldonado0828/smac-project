from datetime import datetime
from copy import deepcopy
from extract import extract_logs

KEY_TRANSACTION =  "id_transaction"
KEY_TIMESTAMP = "timestamp"
KEY_CHANNEL = "channel"
KEY_OPERATION = "operation_type"
KEY_RESPONSE_CODE = "response_code"
KEY_AMOUNT = "amount"
KEY_LATENCY = "latency_ms"

channel_map = {"APP": 1, "SUC" : 2, "ATM" : 3 , "PSE" : 4, "CB": 5}

def transform_logs(data_validate : list[dict]) -> list[dict]:

    transform_data = deepcopy(data_validate)

    for i in range(len(transform_data)):

        channel = transform_data[i][KEY_CHANNEL]
        timestamp = transform_data[i][KEY_TIMESTAMP]


        transform_data[i][KEY_CHANNEL] = channel_map.get(channel)
        transform_data[i][KEY_TIMESTAMP] = datetime.fromisoformat(timestamp)


    return transform_data



if __name__ == "__main__":

    data = extract_logs("logs_example.json")

    transform_data = transform_logs(data)
    
    for i in range(len(transform_data)):
        print(transform_data[i])
