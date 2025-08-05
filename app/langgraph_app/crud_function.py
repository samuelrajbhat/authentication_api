import os
from pathlib import Path
from dotenv import load_dotenv

import httpx

env__path = Path(__file__).resolve().parents[1]/".env"
load_dotenv(dotenv_path=env__path)
API_BASE = os.getenv("API_BASE")



def get_todos(unclean_token: str):
    print(f"unclean tokken>>>> {unclean_token}")
    print(f"API URL {API_BASE}")
    # token = clean_token(unclean_token)
    headers = {"Authorization": f"{unclean_token}"}
    print(f"HEAders: :  {headers}")

    # response = httpx.get(f"{API_BASE}/todos", headers=headers)

 
    response = httpx.get(f"{API_BASE}/todos", headers=headers)

    print(f"responseeeeeee {response.json()}")
    return response.json()
def add_todo(unclean_token:str, title: str, description: str, status: str):
    # token = clean_token(unclean_token)
    headers = {"Authorization": f"{unclean_token}"}
    data = {"title": title, "description": description, "status": status}
    response = httpx.post(f"{API_BASE}/todos", json=data, headers=headers)
    return response.json()

# def update_todo_status(token: str, new_status: str):
    
#     headers = {"Authorization": f"{token}"}