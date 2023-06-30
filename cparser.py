class CParser:
    OPEN_BRACE_CHAR = "{"
    CLOSE_BRACE_CHAR ="}"
    OPEN_PAREN_CHAR = "("
    CLOSE_PAREN_CHAR = ")"
    QUOTE_CHAR = '"'
    SING_LINE_COMMENT_CHAR = "//"
    OPEN_MULTI_LINE_COMMENT_CHAR = "/*"
    CLOSE_MULTI_LINE_COMMENT_CHAR = "*/"
    SEMICOLON = ';'
    WHITESPACE_CHARS = " \t\r\n"
    DELIMETER_CHARS = WHITESPACE_CHARS + OPEN_BRACE_CHAR + CLOSE_BRACE_CHAR + OPEN_PAREN_CHAR + CLOSE_PAREN_CHAR

    @staticmethod
    def parse(lines):
        pass

    @staticmethod
    def __remove_comment(line : str, is_in_multi_line : bool):
        in_string = False
        stripped_line = ""

        #TODO: FIX MULTILINE COMMENT BOUNDS IN QUOTES

        if is_in_multi_line:
            close_comment_char_index = -1
            try:
                close_comment_char_index = line.index(CParser.CLOSE_MULTI_LINE_COMMENT_CHAR)
            except ValueError:
                pass

            if close_comment_char_index != -1:
                line = line[close_comment_char_index + 2:]
                is_in_multi_line = False

            else:
                return stripped_line, is_in_multi_line

        for char in line:
            if char == CParser.COMMENT_CHAR and not in_string:
                return stripped_line, is_in_multi_line
            if char == CParser.QUOTE_CHAR:
                in_string = not in_string
            stripped_line += char

        return stripped_line, is_in_multi_line