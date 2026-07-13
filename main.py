from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph.workflow import graph
from graph.state import GrantState

app = FastAPI(
    title="Grant Review API",
    version="1.0.0"
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Grant Review API is running"
    }


@app.post("/submit")
async def submit_application(application: dict):

    state: GrantState = {
        "application": application,
        "plan": None,
        "tool_results": {},
        "review": None,
        "security_review": None,
        "worker_result": "",
        "final_decision": "",
    }

    result = await graph.ainvoke(state)

    return {
        "decision": result["final_decision"],
        "review": result["review"],
        "security_review": result["security_review"],
        "tool_results": result["tool_results"],
    }