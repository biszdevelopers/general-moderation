"""Moderation classification prompt templates.

The prompt content and the ChatML wrapping live here so they can be tuned
without touching the detector implementation.
"""

from __future__ import annotations

SYSTEM_PROMPT = (
    "You are a strict content moderation classifier. Analyze the user text for "
    "vulgar, abusive, hateful, or politically sensitive content. Reply with "
    "exactly one word: BLOCK or ALLOW."
)

USER_TAG_OPEN = "<user_text>"
USER_TAG_CLOSE = "</user_text>"


def build_classification_prompt(sanitized_payload: str) -> str:
    """Build the ChatML classification prompt around a sanitized payload.

    :param sanitized_payload: sanitized, XML-escaped user text
    :return: the full ChatML prompt
    """
    return (
        "<|im_start|>system\n"
        f"{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"{USER_TAG_OPEN}{sanitized_payload}{USER_TAG_CLOSE}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )
