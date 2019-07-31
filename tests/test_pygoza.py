#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pygoza` package."""

from pathlib import Path

import pytest

from click.testing import CliRunner

from pygoza import cli
from pygoza import __version__


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output
    version_result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert 'version {}'.format(__version__) in version_result.output
    path_result = runner.invoke(cli.main, ['--path /tmp'])
    # assert path_result.
    assert Path('/tmp').exists() is True
