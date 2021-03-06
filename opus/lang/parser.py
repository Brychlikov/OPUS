from lark import Lark
from lark.indenter import Indenter

from pathlib import Path


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4


_current_path = Path(__file__).resolve()
_grammar_fname = _current_path.parent.joinpath("opuslang.lark")
parser = Lark.open(_grammar_fname, parser='lalr', postlex=TreeIndenter(), propagate_positions=True)


if __name__ == '__main__':
    pass


