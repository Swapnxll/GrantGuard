from graph.state import GrantState
from agents.planner import planner_agent
from agents.worker import worker_agent

state: GrantState = {
    "application": {
        "organization": "GreenFuture Foundation",
        "requested_amount": 1500000,
        "registration_valid": True,
        "timeline": "12 months",
        "beneficiaries": 300,
    },
    "plan": None,
    "worker_result": {},
    "final_decision": "",
}

state = planner_agent(state)

print("\nExecution Plan\n")
print(state["plan"])


state = worker_agent(state)
print(state["tool_results"])
