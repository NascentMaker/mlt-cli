"""pytest tests for Restructure class"""

from mlt_cli.restructure import Restructure


def test_get_parser():
    """Test Cliff command"""
    cmd = Restructure(None, None)
    parser = cmd.get_parser("NAME")
    assert parser.prog == "NAME"
