import json

def extract_logs(file_path : str) -> list[dict]:
    with open(file_path,"r",encoding= "utf-8") as file:
        data = json.load(file)
        return data 
    

if __name__ == "__main__":
    data = extract_logs("logs_example.json")
    print(data[0])
    print(len(data))
    print(type(data))


