import re

# Define token types for C++
TOKEN_TYPES = {
    "KEYWORD": r"\b(int|float|if|else|while|for|return|void|char|string|double)\b",
    "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
    "NUMBER": r"\b-?\d+(\.\d+)?(e[+-]?\d+)?\b",  # Fixed regex for numbers + scientific notation
    "STRING": r'"[^"]*"',  # Matches anything inside double quotes
    "OPERATOR": r"[+\-*/=<>!]+",
    "SPECIAL_SYMBOL": r"[{}()\[\],;]",
    "COMMENT": r"//.*|/\*[\s\S]*?\*/"  # Matches single-line (//) and multi-line (/* */) comments
}

def lexical_analyzer(code):
    tokens = []

    # Combine regex patterns
    combined_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES.items())

    for match in re.finditer(combined_regex, code):
        token_type = match.lastgroup
        lexeme = match.group(token_type)

        if token_type != "COMMENT":
            tokens.append((lexeme, token_type))

    return tokens

# Sample C++ code as a string
cpp_code = """
// This is a single-line comment
int main() {
    int x = 10;
    float y = -4.78e2; /* This is a 
    multi-line comment */
    if (x < y) {
        x = x + 1;
        y = x + 3;
    }
    return 0;
}
"""

tokens = lexical_analyzer(cpp_code)

print("\nTokens:")
for i in range(len(tokens)):
    lexeme, token_type = tokens[i]
    print(f"{lexeme} --> {token_type}")