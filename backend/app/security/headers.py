"""Security response headers middleware.

Adds a strict set of HTTP security headers to every response. Incoming
request validation (used by this service's input paths) is performed with the
C-backed ``regex`` module.
"""

from __future__ import annotations

from typing import Any

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

_SECURITY_HEADERS: dict[str, str] = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Content-Security-Policy": (
        "default-src 'none'; "
        "script-src 'self'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "font-src 'self' data:; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'"
    ),
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "X-XSS-Protection": "1; mode=block",
    "Referrer-Policy": "no-referrer",
}


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Attach the security headers to every response."""

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        """Run the request and stamp the security headers on the response.

        :param request: the incoming request
        :param call_next: the downstream ASGI callable
        :return: the response with security headers applied
        """
        response: Response = await call_next(request)
        for header_name, header_value in _SECURITY_HEADERS.items():
            response.headers[header_name] = header_value
        return response
