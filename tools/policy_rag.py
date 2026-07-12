from models.tool_models import ToolResult
import json
from llm import llm
from models.application import GrantApplication
from models.policy_models import PolicyReview
from rag.retriever import PolicyRetriever
from rag.prompts import POLICY_REVIEW_PROMPT

retriever = PolicyRetriever()



def build_query(application: dict) -> str:
    return f"""
    Project Title:
    {application.get("project_title", "")}

    Requested Amount:
    {application.get("requested_amount", "")}

    Beneficiaries:
    {application.get("beneficiaries", "")}

    Timeline:
    {application.get("timeline", "")}
    """

def policy_rag_tool(application: dict) -> ToolResult:
    """
    Retrieve relevant policies and evaluate policy compliance.
    """

    try:
        query = build_query(application)

        retrieved_docs = retriever.retrieve(query)

        policy_context = "\n\n".join(
            f"Source: {doc.metadata.get('source', 'Unknown')}\n{doc.page_content}"
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