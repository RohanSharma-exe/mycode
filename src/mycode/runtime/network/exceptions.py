"""
Networking exceptions.
"""

from __future__ import annotations


class NetworkError(Exception):
    """Base network exception."""


class HTTPRequestError(NetworkError):
    """Raised when an HTTP request fails."""


class HTTPResponseError(NetworkError):
    """Raised when the server returns an error."""
