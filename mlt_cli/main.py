"""Cliff application class for MediaLibraryTools."""

import sys
from pkg_resources import get_distribution

from cliff.app import App
from cliff.commandmanager import CommandManager


class MediaLibraryToolsApp(App):
    """MediaLibraryTools cliff.App implementation"""

    def __init__(self) -> None:
        """Create a new instance of MediaLibraryToolsApp
        :returns: None
        """
        super().__init__(
            description="Media Library Tools",
            version=get_distribution("mlt-cli").version,
            command_manager=CommandManager("cliff.mlt_cli"),
            deferred_help=True,
        )

    def initialize_app(self, _) -> None:
        """Initialize cliff CommandManager app
        :returns: None
        """
        self.LOG.debug("initialize_app")

    def prepare_to_run_command(self, cmd) -> None:
        """Perform preparations for command run
        :param cmd: cliff Command object
        :returns: None
        """
        self.LOG.debug("prepare to run command %s", cmd.__class__.__name__)

    def clean_up(self, cmd, _, err) -> None:
        """Clean up after running the command.
        :param cmd: cliff Command object
        :param err: Error object
        :returns: None
        """
        self.LOG.debug("clean_up %s", cmd.__class__.__name__)
        if err:
            self.LOG.error("got an error: %s", err)


def main(argv=None) -> object:
    """Main script entry point.
    :param argv: Commandline arguments
    :returns: Result from invoked command
    """
    if argv is None:
        argv = sys.argv[1:]
    myapp = MediaLibraryToolsApp()
    return myapp.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
