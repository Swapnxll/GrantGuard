from graph.state import GrantState

from models.judge_models import (
    Decision,
    GrantDecision,
)


def judge_agent(state: GrantState):

    print("\n===== Judge Agent =====")

    review = state["review"]
    security = state["security_review"]
    tool_results = state["tool_results"]

    reasons = []
    recommendations = []

    # ---------------------------------
    # Security Check
    # ---------------------------------

    if not security.safe:

        reasons.append(
            "Security threats detected in the application."
        )

        state["final_decision"] = GrantDecision(
            decision=Decision.REJECT,
            confidence=100,
            reasons=reasons,
            recommendations=[
                "Escalate to manual investigation."
            ],
            summary="Application rejected due to security risks."
        )

        return state

    # ---------------------------------
    # Registration Check
    # ---------------------------------

    registration = tool_results.get("registration")

    if registration and not registration.success:

        reasons.append(
            "Registration verification failed."
        )

        state["final_decision"] = GrantDecision(
            decision=Decision.REJECT,
            confidence=95,
            reasons=reasons,
            recommendations=[
                "Verify NGO registration."
            ],
            summary="Application rejected."
        )

        return state

    # ---------------------------------
    # Quality Check
    # ---------------------------------

    if review.coverage_score < 80:

        reasons.append(
            "Tool execution coverage is too low."
        )

        state["final_decision"] = GrantDecision(
            decision=Decision.MANUAL_REVIEW,
            confidence=80,
            reasons=reasons,
            recommendations=[
                "Complete pending tool executions."
            ],
            summary="Manual review recommended."
        )

        return state

    # ---------------------------------
    # Everything Passed
    # ---------------------------------

    state["final_decision"] = GrantDecision(
        decision=Decision.APPROVE,
        confidence=95,
        reasons=[
            "Application passed automated review."
        ],
        recommendations=[],
        summary="Application approved."
    )

    return state