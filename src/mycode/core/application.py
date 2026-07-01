"""
Application object.

Owns all framework services.
"""

from mycode.core.container import Container
from mycode.core.lifecycle import Lifecycle


class Application:
    """Main application object."""

    def __init__(self) -> None:
        # Dependency injection container.
        self.container = Container()

        # Application lifecycle manager.
        self.lifecycle = Lifecycle()

    async def startup(self) -> None:
        """Start the application."""
        await self.lifecycle.startup()

    async def shutdown(self) -> None:
        """Shutdown the application."""
        await self.lifecycle.shutdown()


# Global application instance.
app = Application()
