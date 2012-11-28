# -*- coding: utf-8 -*-
# typescript.py - sublimelint package for checking TypeScript files

import re

from base_linter import BaseLinter, INPUT_METHOD_TEMP_FILE

CONFIG = {
    'language': 'TypeScript',
    'executable': 'tsc',
    'lint_args': ['{filename}'],
    'input_method': INPUT_METHOD_TEMP_FILE
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        ##print errors
        for line in errors.splitlines():
            match = re.match(r'^.*?\((?P<line>\d+),(?P<column>\d+)\)..(?P<error>.*)', line)
            if match:
                error, line, column = match.group('error'), match.group('line'), match.group('column')
                lineno = int(line)
                columnno = int(column)
                self.underline_word(view, lineno, columnno, errorUnderlines)
                self.add_message(lineno, lines, error, errorMessages)
