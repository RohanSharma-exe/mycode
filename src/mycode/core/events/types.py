"""
Event type definitions.
"""

from collections.abc import Callable

from mycode.core.events.event import Event

EventHandler = Callable[[Event], None]
