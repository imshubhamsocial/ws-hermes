"""GDR40 Code Block Ranges and Metadata Module."""

# Format: (block_id, lang, start_line, end_line, has_lang_header)
# All 1-based inclusive line numbers from original GDR40 doc
RANGES_PART1 = [
    (1, "markdown", 111, 156, False), (2, "markdown", 162, 238, False),
    (3, "bash", 276, 292, True), (4, "markdown", 298, 317, False),
    (5, "yaml", 324, 342, True), (6, "yaml", 344, 349, True),
    (7, "markdown", 351, 368, False), (8, "yaml", 375, 390, True),
    (9, "markdown", 392, 407, False), (10, "yaml", 414, 428, True),
    (11, "markdown", 430, 445, False), (12, "python", 469, 526, True),
    (13, "python", 546, 590, True), (14, "python", 604, 652, True),
    (15, "bash", 679, 697, True)
]

RANGES_PART2 = [
    (16, "bash", 703, 720, True), (17, "javascript", 783, 823, True),
    (18, "javascript", 829, 866, True), (19, "javascript", 872, 907, True),
    (20, "javascript", 913, 961, True), (21, "javascript", 967, 1010, True),
    (22, "bash", 1020, 1055, True), (23, "bash", 1077, 1084, True),
    (24, "bash", 1086, 1103, True), (25, "bash", 1105, 1120, True),
    (26, "python", 1129, 1172, True), (27, "bash", 1174, 1200, True),
    (28, "markdown", 1216, 1255, False), (29, "python", 1258, 1292, True),
    (30, "python", 1294, 1329, True)
]

CODE_RANGES = RANGES_PART1 + RANGES_PART2

def unescape_code_str(code_str: str) -> str:
    escapes = [
        ('\\_', '_'), ('\\-', '-'), ('\\=', '='), ('\\~', '~'),
        ('\\)', ')'), ('\\(', '('), ('\\[', '['), ('\\]', ']'),
        ('\\>', '>'), ('\\<', '<'), ('\\*', '*'), ('\\#', '#'),
        ('\\!', '!'), ('\\$', '$'), ('\\{', '{'), ('\\}', '}'),
        ('\\"', '"'), ("\\'", "'"), ('\\:', ':'), ('\\/', '/'),
        ('\\.', '.'), ('\\+', '+'), ('\\|', '|')
    ]
    for esc, rep in escapes:
        code_str = code_str.replace(esc, rep)
    return code_str
