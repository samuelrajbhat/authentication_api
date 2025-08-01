import os
from pathlib import Path
from dotenv import load_dotenv

import httpx

env__path = Path(__file__).resolve().parents[1]/".env"
load_dotenv(dotenv_path=env__path)
API_BASE = os.getenv("API_BASE")

def get_todos(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{API_BASE}/todos", headers=headers)
    return response.json()

def add_todo(token:str, title: str, description: str, status: str):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "description": description, "status": status}
    response = httpx.post(f"{API_BASE}/todos", json=data, headers=headers)
    return response.json()