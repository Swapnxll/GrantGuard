from graph.state import GrantState

state: GrantState = {
    "application": {
        "organization": "GreenFuture Foundation",
        "requested_amount": 1500000,
        "registration_valid": True,
        "timeline": "12 months",
        "beneficiaries": 300,
    },
    "plan": "",
    "worker_result": "",
    "final_decision": "",
}

print(state)