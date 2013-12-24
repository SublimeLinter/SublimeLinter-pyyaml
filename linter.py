#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2013 NotSqrt
#
# License: MIT
#

"""This module exports the Pyyaml plugin class."""

from SublimeLinter.lint import PythonLinter, persist


class Pyyaml(PythonLinter):

    """Provides an interface to pyyaml."""

    syntax = 'yaml'
    cmd = None
    regex = r'^:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)'
    line_col_base = (0, 0)  # the lines and columns are 0-based
    module = 'yaml'

    def check(self, code, filename):
        """
        Call directly the yaml module, and handles the exception. Return str.

        Very similar to the SublimeLinter-json linter, except yaml is not in the python core library.

        """
        yaml = self.module

        try:
            yaml.safe_load(code)
        except yaml.error.YAMLError as exc:
            if persist.settings.get('debug'):
                persist.printf('{} - {} : {}'.format(self.name, type(exc), exc))
            message = '{} : {} {}'.format(type(exc).__name__, exc.problem, exc.context)
            return ':{}:{}: {}\n'.format(exc.problem_mark.line, exc.problem_mark.column, message)
        except Exception as exc:
            persist.printf('{} - uncaught exception - {} : {}'.format(self.name, type(exc), exc))
        return ''
