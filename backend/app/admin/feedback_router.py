"""Feedback ingestion and manual auto-tuning endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.feedback.feedback_service import FeedbackService


class FeedbackRequest(BaseModel):
    """An administrator correction for one moderation decision.

    :param request_id: the moderated request being corrected
    :param verdict: the verdict the service returned
    :param is_correct: whether that verdict was correct
    :param actual_action: the action the administrator took
    :param severity: severity of the underlying match (0-10), when known
    """

    request_id: str = Field(min_length=1)
    verdict: str = Field(pattern="^(BLOCK|PASS|REVIEW)$")
    is_correct: bool
    actual_action: str = Field(pattern="^(BLOCK|PASS)$")
    severity: int = Field(default=0, ge=0, le=10)


def create_feedback_router(feedback_service: FeedbackService, auth_dependency: Any) -> APIRouter:
    """Build the feedback admin router.

    :param feedback_service: the feedback and auto-tuning service
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(prefix="/admin", tags=["admin"], dependencies=[auth_dependency])

    @router.post("/feedback")
    def feedback(payload: FeedbackRequest) -> dict[str, str]:
        """Record an administrator correction.

        :param payload: the correction
        :return: an acknowledgment
        """
        feedback_service.record_feedback(
            request_id=payload.request_id,
            verdict=payload.verdict,
            is_correct=payload.is_correct,
            actual_action=payload.actual_action,
            severity=payload.severity,
        )
        return {"status": "ok"}

    @router.post("/tune")
    def tune() -> dict[str, Any]:
        """Run the daily weight and threshold tuning batch on demand.

        :return: the tuning report
        :raises HTTPException: 400 when auto-tuning is disabled
        """
        report: dict[str, Any] = feedback_service.run_batch()
        if report.get("status") == "disabled":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Auto-tuning is disabled in the settings",
            )
        return report

    return router
