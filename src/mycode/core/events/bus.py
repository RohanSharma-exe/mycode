"""
Application event bus.
"""

from __future__ import annotations

from collections import defaultdict

from mycode.core.events.event import Event
from mycode.core.events.types import EventHandler


class EventBus:
    """Simple synchronous event bus."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """Register an event handler."""

        self._listeners[event_name].append(handler)

    def publish(self, event: Event) -> None:
        """Publish an event."""

        for handler in self._listeners.get(event.name, []):
            handler(event)

    def clear(self) -> None:
        """Remove all registered handlers."""

        self._listeners.clear()
