from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import *


class ScowlLexer(RegexLexer):
    name = "Scowl"
    aliases = ["scowl"]
    filenames = ["*.scowl"]

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text),  # line continuations
            (r'--(.*?)\n', Comment.Single),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment.Multiline),
            (r'(event)\b', Keyword.Namespace),
            (words((
                'after', 'as', 'because', 'by', 'default', 'exclusive', 'func', 'in', 'is', 'last',
                'map', 'then', 'type', 'when', 'where', 'or', 'and', 'not'), suffix=r'\b'),
             Keyword),
            (r'(true|false|null|inf|second|seconds|minute|minutes|hour|hours|day|days|week|weeks)\b', Keyword.Constant),
            (words(('int', 'float', 'string', 'map',
                    'bool', 'time'), suffix=r'\b'),
             Keyword.Type),
            # float_lit
            (r'\d+(\.\d+[eE][+\-]?\d+|'
             r'\.\d*|[eE][+\-]?\d+)', Number.Float),
            (r'\.\d+([eE][+\-]?\d+)?', Number.Float),
            # int_lit
            (r'(0|[1-9][0-9]*)', Number.Integer),
            # JSONPath string
            (r'\$\S*', String.Other),
            # StringLiteral
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
            # Tokens
            (r'(<=|>=|='
             r'|!=|//|:=|[+\-*/%])', Operator),
            (r'[|^<>=!()\[\]{}.,;:]', Punctuation),
            # identifier
            (r'[A-Z]\w*', Name.Function),
            (r'[^\W\d]\w*', Name.Other),
        ]
    }


__all__ = ['ScowlLexer']
