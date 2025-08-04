import os
from pathlib import Path
from dotenv import load_dotenv

import httpx

env__path = Path(__file__).resolve().parents[1]/".env"
load_dotenv(dotenv_path=env__path)
API_BASE = os.getenv("API_BASE")

def clean_token(token: str) -> str:
    if token.startswith("Bearer "):
        return token.split("bearer ")[1]
    return token


def get_todos(unclean_token: str):
    print(f"unclean tokken>>>> {unclean_token}")
    print(f"API URL {API_BASE}")
    token = clean_token(unclean_token)
    headers = {"Authorization": f"Bearer {token}"}
    print(f"HEAders: :  {headers}")

    # response = httpx.get(f"{API_BASE}/todos", headers=headers)

    try:
        response = httpx.get(f"{API_BASE}/todos", headers=headers)
        return response
    except Exception as e:
        print(">>> JSON decode error:", str(e))
        raise

def add_todo(unclean_token:str, title: str, description: str, status: str):
    token = clean_token(unclean_token)
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "description": description, "status": status}
    response = httpx.post(f"{API_BASE}/todos", json=data, headers=headers)
    return response.json()