"""Cliff command module for the Restructure command"""

import io
import logging
import os
import re

from cliff.command import Command
from cliff._argparse import ArgumentParser


class Restructure(Command):
    """Restructure all files in the designated parent directory."""

    log = logging.getLogger(__name__)
    outfile: io.TextIOWrapper
    filenames = []
    statement_regex = re.compile("(use|include) <[^>]+>")

    def get_parser(self, prog_name) -> ArgumentParser:
        """Set up and return the parser.
        :param prog_name: name of program
        """
        parser = super().get_parser(prog_name)
        parser.add_argument("filename", nargs="?")
        return parser

    def take_action(self, parsed_args) -> int:
        """Perform action on file
        :param parsed_args: structure of parsed arguments
        :returns: None
        """
        self.log.debug("parsed_args: %s", parsed_args)
        try:
            infile = os.path.abspath(parsed_args.filename)
            if not os.path.exists(infile):
                self.log.error("No such file or directory.")
                return 127
            self.log.info("take_action: %s", parsed_args, exc_info=True)
            return 0
        except (FileNotFoundError, TypeError) as ex:
            if isinstance(ex, FileNotFoundError):
                self.log.error("No such file or directory.")
                return 127
            self.log.error("Please enter a filename.")
            return 1
