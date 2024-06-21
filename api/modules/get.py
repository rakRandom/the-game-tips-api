from api.api import *

def json_get_data(path: str):
    file_content: dict
    
    with open(f"api/data/{path}", "r", encoding="UTF-8") as file:
        file_content = load(file)
    
    if file_content:
        return file_content
    return
