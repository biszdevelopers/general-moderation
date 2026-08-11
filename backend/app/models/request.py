"""Incoming moderation request models.

Validation is delegated to Pydantic v2, whose core engine is implemented
in Rust.
"""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class ModerationRequest(BaseModel):
    """A single message to moderate.

    :param id: caller-supplied identifier echoed back in the response
    :param user_id: identifier of the author, used for auditing
    :param text: the message body to moderate
    """

    id: str | None = None
    user_id: str | None = None
    text: Annotated[str, Field(min_length=1, max_length=8192)]


class BatchItem(BaseModel):
    """One entry in a batch moderation request.

    :param id: caller-supplied identifier echoed back in the response
    :param user_id: identifier of the author, used for auditing
    :param text: the message body to moderate
    """

    id: str | None = None
    user_id: str | None = None
    text: Annotated[str, Field(min_length=1, max_length=8192)]


class BatchModerationRequest(BaseModel):
    """A list of messages to moderate in a single request.

    :param items: the messages to moderate
    """

    items: Annotated[list[BatchItem], Field(min_length=1, max_length=100)]
