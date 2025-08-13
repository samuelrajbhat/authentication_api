from fastapi import APIRouter,status, Depends, HTTPException, Request
from fastapi.responses import StreamingResponse
from .agent_graph import run_graph
from .agent_models import LLMRequest


langgraph_router = APIRouter(prefix="/ai")


@langgraph_router.post("/ask")
def ask_agent(request_data: LLMRequest,
              request: Request):
    token = request.headers.get("Authorization")
    print("kjkdf", token)
    print ("mhms jflksmmf >> ---", request_data.messages)
    if not token: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization token required")

    # response = run_graph(request_data.messages, token)
    return StreamingResponse(run_graph(request_data.messages, token), media_type= "text/plain")