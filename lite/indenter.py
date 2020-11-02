from lark.indenter import Indenter

class LiteIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = ['LPAR', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RBRACE']
    INDENT_TYPE = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8