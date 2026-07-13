import json

from llm import llm
from models.policy_models import PolicyReview
from models.tool_models import ToolResult
from rag.prompts import POLICY_REVIEW_PROMPT
from rag.retriever import PolicyRetriever


retriever = PolicyRetriever()


def build_query(application: dict) -> str:
    """
    Build a semantic retrieval query from the grant application.
    """

    budget_summary = "\n".join(
        f"- {category}: ₹{amount:,}"
        for category, amount in application.get("budget", {}).items()
    )

    documents = ", ".join(application.get("documents", []))

    return f"""
Organization:
{application.get("organization", "")}

Project Title:
{application.get("project_title", "")}

Grant Category:
{application.get("grant_category", "")}

Project Description:
{application.get("project_description", "")}

Requested Amount:
₹{application.get("requested_amount", 0):,}

Beneficiaries:
{application.get("beneficiaries", 0)}

Timeline:
{application.get("timeline", "")}

Budget Breakdown:
{budget_summary}

Supporting Documents:
{documents}
""".strip()


def policy_rag_tool(application: dict) -> ToolResult:
    """
    Retrieve relevant policy documents and evaluate policy compliance.
    """

    try:
        query = build_query(application)

        retrieved_docs = retriever.retrieve(query)

        policy_context = "\n\n".join(
    f"""
====================================================
Policy File: {doc.metadata.get("source", "Unknown")}
====================================================

{doc.page_content}
"""
    for doc in retrieved_docs
)

        prompt = POLICY_REVIEW_PROMPT.format(
            application=json.dumps(application, indent=2),
            policy_context=policy_context,
        )

        review = (
            llm.with_structured_output(PolicyReview)
            .invoke(prompt)
        )

        return ToolResult(
            tool="policy_rag",
            status="SUCCESS",
            success=True,
            reason="Policy compliance evaluation completed.",
            data=review.model_dump(),
        )

    except Exception as e:
        return ToolResult(
            tool="policy_rag",
            status="FAILED",
            success=False,
            reason=f"Policy evaluation failed: {str(e)}",
            data={},
        )