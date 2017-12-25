import os, re

FILE_PATH = ''

def analyze_code(codefilesource):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(codefilesource) as f:
        lines = f.readlines()
        total_line = len(lines)
        line_index = 0
        while line_index < total_line:
            line = lines[line_index]
            if line.startswith('#'):
                comment_line += 1
            elif re.match("\s*'''",line) is not None:
                comment_line += 1
                while re.match(".*'''$",line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            elif line == "\n":
                blank_line += 1
            line_index += 1
    return [total_line,comment_line,blank_line]
def run(filepath):
    os.chdir(filepath)
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            line = analyze_code(i)
            total_lines, total_comment_lines, total_blank_lines = total_lines + line[0], total_comment_lines + line[1], total_blank_lines + line[2]