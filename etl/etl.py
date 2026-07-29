from extract import extract_logs
from validate import is_validate
from transform import transform_logs
from load import load_logs
from datetime import datetime

if __name__ == "__main__":

    try:
        file_path = "generator/logs_example.json"

        data = extract_logs(file_path)

        validate_data , invalidate_data = is_validate(data)

        transform_data = transform_logs(validate_data)

        load_logs(transform_data)

        print("=======================================")
        print("EJECUCION DEL PIPELINE")
        print("=======================================")

        print(f"Inicio: {datetime.now().isoformat()}")

        print(f"\nTransacciones generadas : {len(data)}")

        print(f"\nTransacciones validas : {len(validate_data)}")
        print(f"Transacciones invalidas : {len(invalidate_data)}")

        print("\nEstado: Se ejecuto correctamente")

    except Exception as e:

        print("=======================================")
        print("EJECUCION DEL PIPELINE")
        print("=======================================")

        print("\nESTADO: No se pudo ejecutar correctamente")

        print(f"\nMotivo: {e}")



