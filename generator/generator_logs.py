import json
from datetime import datetime, timedelta
from random import choices, randint , gauss

'''
log = {
    "id_transaccion": "TX123456789",
    "timestamp": "2024-06-15T12:34:56Z",
    "canal": "App Movil",
    "tipo_operacion": "Transferencia",
    "codigo_respuesta": "00",
    "monto": 1000000,
    "latencia_ms": 340
}
print(json.dumps(log,indent = 2,ensure_ascii=False))
'''
def generate_log(identify_number:int, timestamp:datetime):
    channel = ["APP","SUC","PSE","ATM","CB"]
    operation_type = ["BALANCE_INQUIRY","TRANSFER","PAYMENT","WITHDRAWAL"]
    response_code = ["00","51","91","96","68"]
    performance = ["NORMAL_MODE","SLOW_MODE"]
    mode = choices(performance,weights=[95,5],k=1)[0]
    if mode == "NORMAL_MODE":
        latency_ms = max(80,int(gauss(250,70)))
    else:
        latency_ms = max(500,(int(gauss(2200,400))))
    log = {
            "id_transaction" : f"TX-{identify_number:06d}",
            "timestamp" : timestamp.isoformat(),
            "channel" : choices(channel,weights=[45,15,20,12,8],k=1)[0],
            "operation_type" : choices(operation_type,weights=[40,35,20,5],k=1)[0],
            "response_code" : choices(response_code,weights=[95,2,1,1,1],k=1)[0],
            "amount": randint(10000,3000000),
            "latency_ms" : latency_ms
    }
    return log

register_number = 10
timestamp = datetime(2026,7,8,8,34,56)
register = []
for i in range(register_number):
    register.append(generate_log(i+1, timestamp))
    timestamp += timedelta(seconds=2)

with open("logs_example.json","w", encoding="utf-8") as file:
    json.dump(register, file , indent = 2, ensure_ascii=False)
