import re
keywords = {"int", "float", "double", "char", "void","long", "short", "signed", "unsigned","bool", "string", "if", "else", "while",
    "for", "return", "break", "continue","switch", "case", "default", "do"}
operators = {"==", "!=", "<=", ">=", "++", "--","+", "-", "*", "/", "%", "=","<", ">", "&&", "||", "!"}
symbols = {"(", ")", "{", "}", ";", ",", "[", "]"}
token_pattern = r'==|!=|<=|>=|\+\+|--|&&|\|\||[+\-*/%=<>!;(),{}\[\]]|\d+\.\d+|\d+|[A-Za-z_][A-Za-z0-9_]*'
def lexical_analyzer(code):
    tokens = re.findall(token_pattern, code)
    result = []
    for token in tokens:
        if token in keywords:
            result.append((token, "Keyword"))
        elif token in operators:
            result.append((token, "Operator"))
        elif token in symbols:
            result.append((token, "Symbol"))
        elif token.isdigit():
            result.append((token, "Integer"))
        elif re.match(r'^\d+\.\d+$', token):
            result.append((token, "Float"))
        elif token.isidentifier():
            result.append((token, "Identifier"))
        else:
            result.append((token, "Unknown"))
    return result
print("Enter source code line by line.")
print("Type END on a new line to finish:\n")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)
code = "\n".join(lines)
tokens = lexical_analyzer(code)
print("\nTokens:")
for token, token_type in tokens:
    print(f"{token:12} --> {token_type}")

print(f"\nTotal Tokens: {len(tokens)}")
