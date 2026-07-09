from graph.state import GrantState
from agents.planner import planner_agent
from agents.worker import worker_agent
from graph.workflow import graph

state: GrantState = {
    "application": {
        "organization": "GreenFuture Foundation",
        "requested_amount": 150000000,
        "registration_valid": False,
        "timeline": "12 months",
        "beneficiaries": 300,
    },
    "plan": None,
    "tool_results": {},
    "worker_result": "",
    "final_decision": "",
}

# state = planner_agent(state)

# print("\nExecution Plan\n")
# print(state["plan"])


# state = worker_agent(state)
# print(state["tool_results"])

result = graph.invoke(state)

print("\n===== TOOL RESULTS =====")

for tool_name, tool_result in result["tool_results"].items():
    print(f"\n🔹 {tool_name}")
    print(f"Status : {tool_result.status}")
    print(f"Success: {tool_result.success}")
    print(f"Reason : {tool_result.reason}")
    print(f"Data   : {tool_result.data}")


review = result["review"]

print("\n===== QUALITY REVIEW =====")
print(f"Passed            : {review.passed}")
print(f"Coverage Score    : {review.coverage_score}")
print(f"Evidence Score    : {review.evidence_score}")
print(f"Confidence Score  : {review.confidence_score}")
print(f"Missing Tools     : {review.missing_required_tools}")
print(f"Failed Tools      : {review.failed_tools}")
print(f"Strengths         : {review.strengths}")
print(f"Weaknesses        : {review.weaknesses}")
print(f"Summary           : {review.summary}")

# Receive State

# ↓

# Planner Node

# ↓

# Update State

# ↓

# Worker Node

# ↓

# Update State

# ↓

# Return Final State
