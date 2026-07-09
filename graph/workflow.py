from langgraph.graph import StateGraph, START, END

from graph.state import GrantState
from agents.planner import planner_agent
from agents.worker import worker_agent
from agents.reviewer import reviewer_agent

builder = StateGraph(GrantState)

# Add nodes
builder.add_node("planner", planner_agent)

# Planner Node
#       │
#       ▼
# planner_agent(state)

builder.add_node("worker", worker_agent)

# Planner
#   ↓
# Worker

builder.add_node("reviewer", reviewer_agent)

# Define execution flow
builder.add_edge(START, "planner")
builder.add_edge("planner", "worker")
builder.add_edge("worker", "reviewer")
builder.add_edge("reviewer", END)

graph = builder.compile()