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

def generate_log():
    timestamp = datetime(2026,7,8,8,34,56)
    channel = ["APP","SUC","PSE","ATM","CB"]
    opperation_type = ["BALANCE_INQUIRY","TRANSFER","PAYMENT","WITHDRAWAL"]
    response_code = ["00","51","91","96","68"]
    for i in range (1,10):
        log = {
            "id_transaction" : f"TX-{i:06d}",
            "timestamp" : timestamp.isoformat(),
            "channel" : choices(channel,weights=[45,15,20,12,8],k=1)[0],
            "operation_type" : choices(opperation_type,weights=[40,35,20,5],k=1)[0],
            "response_code" : choices(response_code,weights=[95,2,1,1,1],k=1)[0],
            "amount": f"${randint(10000,3000000):,}",
            "latency_ms" : round(gauss(200,30),3)
        }
        print(json.dumps(log,indent = 2,ensure_ascii=False))
        timestamp += timedelta(seconds=2)

generate_log()