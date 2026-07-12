from typing import List
from pydantic import BaseModel, Field


class PolicyFinding(BaseModel):
    """
    A single policy compliance finding.
    """

    policy_name: str = Field(
        description="Name of the policy document."
    )

    status: str = Field(
        description="COMPLIANT, NON_COMPLIANT, or NEEDS_REVIEW."
    )

    explanation: str = Field(
        description="Explanation of the finding."
    )

    evidence: str = Field(
        description="Relevant policy excerpt supporting the finding."
    )


class PolicyReview(BaseModel):
    """
    Overall policy compliance review.
    """

    compliant: bool = Field(
        description="Whether the application complies with all relevant policies."
    )

    findings: List[PolicyFinding] = Field(
        default_factory=list,
        description="List of policy findings."
    )

    summary: str = Field(
        description="Overall summary of the policy review."
    )