# This file is placed in the public domain or under the
# CC0-1.0-Universal license, whichever is more permissive.

"""Custom lexer for PEP XXX Match expression."""

import keyword

from pygments.lexer import DelegatingLexer, bygroups, default, this, using
from pygments.lexers.python import (
    PythonLexer,
    PythonTracebackLexer,
    _PythonConsoleLexerBase,
)
from pygments.token import Keyword, Other, Text, Whitespace


class PyMatchExprLexer(PythonLexer):
    name = "pyMatchExpr"

    # fmt: off
    tokens = {
        "soft-keywords": [
            # `match`, `case` and `_` soft keywords
            (r"(^[ \t]*)"              # at beginning of line + possible indentation
             r"(match|case)\b"         # a possible keyword
             r"(?![ \t]*(?:"           # not followed by...
             r"[:,;=^&|@~)\]}]|(?:" +  # characters and keywords that mean this isn't
                                       # pattern matching (but None/True/False is ok)
             r"|".join(k for k in keyword.kwlist if k[0].islower()) + r")\b))",
             bygroups(Text, Keyword), "soft-keywords-inner"),
            (r"(^[ \t]*)"              # at beginning of line + possible indentation
             r"(.*)"                   # subject expression
             r"\b(match)\b",           # match keyword
             bygroups(Whitespace, using(this), Keyword), "soft-keywords-inner"),
        ],
        "soft-keywords-inner": [
            # optional `_` keyword
            (r"(\s+)([^\n_]*)(_\b)", bygroups(Whitespace, using(this), Keyword)),
            default("#pop"),
        ],
    }
    # fmt: on


class PyMatchExprConsoleLexer(DelegatingLexer):
    name = "pyMatchExpr-console"

    def __init__(self, **options):
        pylexer = PyMatchExprLexer
        tblexer = PythonTracebackLexer

        class _ReplaceInnerCode(DelegatingLexer):
            def __init__(self, **options):
                super().__init__(
                    pylexer, _PythonConsoleLexerBase, Other.Code, **options
                )

        super().__init__(tblexer, _ReplaceInnerCode, Other.Traceback, **options)


def register():
    return [PyMatchExprLexer]
