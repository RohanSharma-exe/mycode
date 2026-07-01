"""
Framework bootstrap.
"""

from __future__ import annotations

from mycode.app.application import Application


def bootstrap() -> Application:
    """
    Build the application.

    Every shared service is created here.
    """

    application = Application()

    return application
