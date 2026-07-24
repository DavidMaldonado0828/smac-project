from  extract import  extract_logs
from datetime import datetime
import re

def is_duplicate_transaction(id: str, seen_ids: set) -> bool:
    if id in seen_ids:
        return True
    seen_ids.add(id)
    return False

def is_format_correct_transaction_id(id: str) -> bool:
    id_format = r"^TX-\d{6}$"
    return re.match(id_format, id) is not None

def is_format_correct_timestamp(timestamp: str) -> bool:
    try:
        datetime.fromisoformat(timestamp)
        return True
    except ValueError:
        return False

def is_valid_category(value: str, valid_options: set) -> bool:
    return value in valid_options

def is_valid_amount(amount: int) -> bool:
    if isinstance(amount, int) and 10000 <= amount <= 3000000:
        return True
    return False

def is_valid_latency(latency: int) -> bool:
    if isinstance(latency, int) and 1 <= latency <= 10000:
        return True
    return False

KEY_TRANSACTION =  "id_transaction"
KEY_TIMESTAMP = "timestamp"
KEY_CHANNEL = "channel"
KEY_OPERATION = "operation_type"
KEY_RESPONSE_CODE = "response_code"
KEY_AMOUNT = "amount"
KEY_LATENCY = "latency_ms"

def is_validate(data : list[dict]) -> tuple[list[dict], list[dict]]:
    seen_ids = set()
    channel_type = {"APP","SUC","PSE","ATM","CB"}
    operation_type = {"BALANCE_INQUIRY","TRANSFER","PAYMENT","WITHDRAWAL"}
    response_code = {"00","51","91","96","68"}
    validate = []
    invalidate = []
    
    for i in range (len(data)):
        incorrect_log = {}
        is_correct = True
        id = data[i][KEY_TRANSACTION]
        timestamp = data[i][KEY_TIMESTAMP]
        channel = data[i][KEY_CHANNEL]
        operation = data[i][KEY_OPERATION]
        code = data[i][KEY_RESPONSE_CODE]
        amount = data[i][KEY_AMOUNT]
        latency = data[i][KEY_LATENCY]
        if is_duplicate_transaction(id, seen_ids):
            incorrect_log.setdefault(KEY_TRANSACTION, []).append(f"The id {id} is duplicate")
            is_correct = False
        if not is_format_correct_transaction_id(id):
            incorrect_log.setdefault(KEY_TRANSACTION, []).append(f"The id {id} has an incorrect format")
            is_correct = False
        if not (is_format_correct_timestamp(timestamp)):
            incorrect_log[KEY_TIMESTAMP] = f"The timestamp to break the format"
            is_correct = False
        if not (is_valid_category(channel,channel_type)):
            incorrect_log[KEY_CHANNEL] = f"The channel {channel} doesn't exist"
            is_correct = False
        if not (is_valid_category(operation,operation_type)):
            incorrect_log[KEY_OPERATION] = f"The operation {operation} doesn't exist"
            is_correct = False
        if not (is_valid_category(code,response_code)):
            incorrect_log[KEY_RESPONSE_CODE] = f"The code {code} doesn't exist"
            is_correct = False
        if not (is_valid_amount(amount)):
            incorrect_log[KEY_AMOUNT] = f"The amount {amount} is out of the range between 10000 and 3000000"
            is_correct = False
        if not(is_valid_latency(latency)):
            incorrect_log[KEY_LATENCY] = f"The latency {latency} is out of the range between 1 and 10000"
            is_correct = False

        if (is_correct):
            validate.append(data[i])
        else:
            invalidate.append(incorrect_log)

    return validate,invalidate




if __name__ == "__main__":
    data = extract_logs("logs_example.json")
    validos, invalidos = is_validate(data)

    print("==================validate================")
    print(validos[0])
    print(len(validos))
    print(type(validos))

    print("=================Invalidate===============")
    try:
        print(invalidos[0])
    except IndexError:
        print("No hay ninguno inválido")
    print(len(invalidos))
    print(type(invalidos))


       

     
