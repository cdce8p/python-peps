from __future__ import annotations

from typing import TYPE_CHECKING

from .asdl_lexer import ASDLLexer
from .pep823_lexar import Py823ConsoleLexer, Py823Lexer
from .pep824_lexar import Py824Lexer

if TYPE_CHECKING:
    from pygments.lexer import Lexer

__all__ = ("pep_lexers",)

pep_lexers: list[type[Lexer]] = [
    ASDLLexer,
    Py823ConsoleLexer,
    Py823Lexer,
    Py824Lexer,
]
